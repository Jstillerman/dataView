#pragma strict
import SimpleJSON;

var data : WWW = null; //Initiate a WWW
var numberOfObjects = 0.0;
var timeStep = 0;
var vanilla = true;
var N = JSON.Parse("");

public var cubePref: GameObject;
public var url = "http://www.psfc.mit.edu/~jas/genray_scaled.json";
				 //This is changeable based on clients needs.
var colors = [Color.red, Color.green, Color.blue, Color.magenta, Color.white, Color.cyan, Color.yellow];
var tags   = ["alpha", "bravo", "zeta", "beta", "panda", "chicken", "fish", "Apricot"];
public var show = [false, false, false, false, false, false, false];




function Start () {


url = System.IO.File.ReadAllText("C:\\Users\\Jason\\Documents\\Programming\\dataView\\VANNILLAUNITYTEST\\settings.temp");

data = new WWW(url); //THIS ACTUALL FETCHES THE DATA



}

function Update () {
if(data.isDone && vanilla){
	Debug.Log(data.text);
	N = JSON.Parse(data.text);
	numberOfObjects = N["nray"].AsFloat;
	InvokeRepeating("thing", 0.001, 0.001);

}

//OTHER UPDATE STUFF

for (var i = 0; i < 7; i ++){
var key = i.ToString();

if(Input.GetKeyDown(key)){
Debug.Log(key + " key down");
var parsed = int.Parse(key) - 1;
 var cubes = GameObject.FindGameObjectsWithTag(tags[parsed]);

 for (cube in cubes){
 cube.GetComponent.<Renderer>().enabled = show[parsed];
 }
  show[parsed] = show[parsed] ? false : true;

}
}

 		  var hit : RaycastHit;
       var fwd = transform.position;
		if (Physics.Raycast (transform.position, fwd, hit)) {
		hit.collider.gameObject.GetComponent.<Renderer>().material.color = Color.white;
		}



/////
}

function thing(){
vanilla = vanilla ? false: false; //TOGGLE ON AND OFF VANILLA



if (data.isDone){

for (var i = 0; i < numberOfObjects; i++){
	var pos = new Vector3();
	pos.z = N["values"]["wx"][i][timeStep].AsFloat;
	pos.x = N["values"]["wy"][i][timeStep].AsFloat;
	pos.y = N["values"]["wz"][i][timeStep].AsFloat;

	if(pos.x + pos.y +pos.z != 0){
	var sphere : GameObject = Instantiate(cubePref);
	sphere.transform.position = pos;


	var values = "";
	for (name in N["names"]){
	var realName = name.ToString()[0:-1][1:];

	values += realName + ": " + (N["values"][realName][i][timeStep].AsFloat) + "\n";
	}

	//Debug.Log(values);

	//var identification = sphere.gameObject.AddComponent ("ident");

	//UnityEngineInternal.APIUpdaterRuntimeServices.AddComponent (sphere, "Assets/mainScript.js(95,9)", "raycast");
	//UnityEngineInternal.APIUpdaterRuntimeServices.AddComponent (sphere, "Assets/mainScript.js(96,9)", "raycast");
	//Debug.Log(MeshRenderer);
	sphere.BroadcastMessage("addValue", values);
	var sizekey = N["sizekey"].Value;
	Debug.Log(sizekey);
	var size = N["values"][sizekey][i][timeStep].AsFloat;

	var hue = N["values"][N["colorkey"].Value][i][timeStep].AsFloat;


	var myColor = Color.red;
	myColor.r = hue;



	sphere.GetComponent.<Renderer>().material.color = myColor;

	size *= size;
	size /= 2;
	sphere.transform.localScale = new Vector3(size, size, size);
	sphere.tag = tags[i];

	//sphere.GetComponent(Renderer).material.color = colors[i];

	}

}

timeStep++;
}

}




///// NOTES
///// color - conversion done still need this set up
///// size  - all done on your part
///// gui   - doesnt want to iterate :[
