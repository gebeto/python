import * as React from 'react';
import ReactDOM from 'react-dom';

import { Client as Styletron } from 'styletron-engine-atomic';
import { Provider as StyletronProvider } from 'styletron-react';
import { LightTheme, DarkTheme, BaseProvider, styled } from 'baseui';
import { StatefulInput } from 'baseui/input';
import { Display2 } from 'baseui/typography';

import { Auth } from './Auth';
// import { Upload } from './Upload';


const engine = new Styletron();

const Centered = styled('div', {
	display: 'flex',
	flexDirection: 'column',
	justifyContent: 'center',
	alignItems: 'center',
	height: '100vh',
});

const Body = styled('div', {
	display: 'flex',
	maxWidth: '500px',
});


export const App = ({ children }: any) => {
	return (
		<StyletronProvider value={engine}>
			<BaseProvider theme={LightTheme}>
				<Centered>
					<Display2 marginBottom="scale500">Pocket tools</Display2>
					<Body>
						<Auth />
					</Body>
				</Centered>
			</BaseProvider>
		</StyletronProvider>
	);
}


ReactDOM.render(<App />, document.querySelector("#root"));
