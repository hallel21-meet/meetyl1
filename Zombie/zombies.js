function tooSlow(){
	setTimeout(
		function(){
			alert("You're dead!!! you were too slow!!!");
			restart()
		} , 7000);
}

function restart() {
	setTimeout(
		function(){
			if (confirm("Would you like to play again?")) {
    			window.location.replace("zombie.html");
			} else {
    			window.location.replace("theEnd.html");
			}
		} , 1000);
}
