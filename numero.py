#!/usr/bin/python3
import os
def verificar(num):
	if(num>10):
		resultado = ('O seu numero {} eh maior do que 10!'.format(num))
	elif(num<10):
		resultado = ('O seu numero {} eh menor do que 10!'.format(num))
	else:
		resultado = ('O seu numero eh exatamente {}'.format(num))
	return resultado

QUERY = os.getenv('QUERY_STRING')
num = int(QUERY.split('=')[1])
resultado = verificar(num)

print('Content-type:text/html\r\n\r\n')
print(' <!DOCTYPE html>')
print(' <html >')
print(' <head>')
print(' <meta charset="UTF-8" />')
print(' <title>Pratica CGI</title>')
print(' <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">')
print(' <style>')
print('  body { ')
print('  background-color: #66ffcc;')
print('  }')
print('  </style>')
print('  </head>')
print(' <body>')
print('  <div class="card container" style="margin-top: 200px;">')
print('  <div class="card-header container" style="font-weight: bold; background-color: white;">')
print('      Descubra se o numero e maior!')
print('  </div>')
print('  <div class="card-body container">')
print('  <h5 class="card-title">Informe um numero para saber se ele e maior do que 10</h5>')
print('  <form action="/cgi-bin/numero.py" id="formNumero" method="GET">')
print('  <label>Digite o numero aqui</label>')
print('  <input type="text" name="numero" id="numero" required="required">')
print('  <button type="submit" class="btn btn-primary">ENVIAR</button>')
print('  </form>')
print('  <p>')
print('  <div class="alert alert-success" role="alert"> <strong>{}</strong>'.format(resultado))
print('  </div>')
print('  </div>')
print('  </div>')
print('  <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>')
print('  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>')
print('  <script type="text/javascript" src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>')
print('  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jquery-validation@1.19.2/dist/jquery.validate.min.js"></script>')
print('  <script type="text/javascript">')
print('  (function( factory ) {')
print('  if ( typeof define === "function" && define.amd ) {')
print('  define( ["jquery", "../jquery.validate"], factory );')
print('  } else if (typeof module === "object" && module.exports) {')
print('  module.exports = factory( require( "jquery" ) );')
print('  } else {')
print('  factory( jQuery );')
print('  }')
print('  }(function( $ ) {')
print('  $.extend( $.validator.messages, {')
print('  required: "Este campo eh obrigatorio.",')
print('  number: "Oh meu fie, eh para colocar um tipo numerico e n uma letra...",')	
print('  } );')
print('  return $;')
print('  }));')
print('  </script>') 
print('  <script>')
print('  $(document).ready(function() {')
print('  $("#formNumero").validate({')
print('  rules:{')
print('  numero: {')
print('  required: true,')
print('  number: true,')
print('  maxlength: 10000000000000000000000000')
print('  }')
print('  }')
print('  })')
print('  })')
print('  </script>')
print('  </body>')
print('  </html>')
