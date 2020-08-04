# passer une commande 
exec {'pkill killmenow':
provider => 'shell'
}