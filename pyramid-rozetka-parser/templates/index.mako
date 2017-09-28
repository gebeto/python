# -*- coding: utf-8 -*- 
## <%inherit file="layout.mako"/>
<!DOCTYPE html>  
<html>
<head>
  <meta charset="utf-8">
  <title>Pyramid Rozetka Parser</title>
  <meta name="viewport" content="width=device-width">
  <meta name="viewport" content="initial-scale=1.0">

  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.css">
  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap-theme.css">
  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-slider/9.5.3/css/bootstrap-slider.min.css">
  <link rel="stylesheet" href="static/css/style.css">

</head>

<body>
  <div class="container">
    <div class="col-md-6 col-md-offset-3">
    <!-- header -->
      <div class="row logo">
        <center>
          <img src="http://i1.rozetka.ua/logos/0/99.png">
        </center>
      </div>

    <!-- form  -->
      <form action="#" method="GET">
        <div class="input-group col-md-12">
          <span class="input-group-btn">
          <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
          	<span class="caret"></span>
          	http://
          </button>
          <ul class="dropdown-menu">
          	<li><a href="">hard.rozetka.com.ua/processors/intel/c80083/v336/</a></li>
          	<li><a href="">hard.rozetka.com.ua/ssd/c80109/</a></li>
          	<li><a href="">hard.rozetka.com.ua/videocards/c80087/21349=4241/</a></li>
          	<li><a href="">rozetka.com.ua/mobile-phones/c80003/filter/preset=flagman_smartphones;producer=apple/</a></li>
          	<li><a href="">rozetka.com.ua/tablets/c130309/filter/</a></li>
          </ul>
          </span>
          <input class="form-control" type="text" name="url" value="rozetka.com.ua/stabilizers/c144719/" placeholder="url">
          <span class="input-group-addon glyphicon ">
            <input type="checkbox" name="json" title="JSON">
          </span>
        </div>
        <input class="form-control btn btn-default" type="submit" value="Парсити">
      </form>
    
    <!-- products  -->
      <div class="products">
        
        % if products:
          <!-- price range -->
          <input id="price" type="text" class="price-slider" style="width: 100%">
        % endif

        <!-- items start -->
        <div class="items">

          % if products:
            % for product in products:
              <div class="card" price="${product['price']}">
              <div class="card-block">
                <h4 class="card-title">$${product['price']}</h4>
                <h6 class="card-subtitle text-muted">${product['name']}</h6>
              </div>
              </div>
            % endfor
          % elif error:
            <div>Помилка! Щось пішло не так!</div>
          % else:
            <div>Нічого не знайдено</div>
          % endif

        </div>
        <!-- items end -->
      </div>
    </div>
  </div>

<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-slider/9.5.3/bootstrap-slider.min.js"></script>
<script src="static/js/app.js"></script>

% if products:
  <script type="text/javascript">
  	if ($("#price")) {
      $("#price").slider({
        min:${products[0]['price']},
        max:${products[-1]['price']},
        value:[
          ${products[0]['price']},
          ${products[-1]['price']}
        ],
        step:0.01});
      }
  </script>
% endif

</body>
</html>