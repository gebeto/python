import React, { Component } from 'react';
import './App.css';
import data from './work_data.json';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      search: '',
      time: false,
    }
    this.input = this.input.bind(this);
  }

  getSource = () => {
    let result = data.tags.filter((item) => {
      if (this.state.search.length === 0 || item.includes(this.state.search)) {
        return true;
      }
    }).map((item, index) => {
      return data.works.filter((work) => {
        if (work.tags.includes(item)) {
          return true;
        }
      }).map((work, index) => {
        return work;
      });
    });
    let res = {};
    for (let i = 0; i < result.length; i++) {
      for (let j = 0; j < result[i].length; j++) {
        res[result[i][j].url] = result[i][j];
      }
    }
    return Object.values(res);
  }

  input(e) {
    let time = new Date();
    this.setState({
      search: e.target.value,
      time: time,      
    });
  }

  render() {
    const source = this.getSource();
    return (
      <div className="App">

        <input type="text" onChange={this.input}/>
        <h2>{source.length}</h2>

        <ul>
          {source.map((work, index) => {
            return ((<li key={index}>
          <a href={work.url} target="_blank">{work.title}</a>
        </li>));
          })}
        </ul>
      </div>
    );
  }
}

export default App;
