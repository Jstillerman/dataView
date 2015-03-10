#pragma strict

var areas = [Vector3(0,0,0), Vector3(172.6, 17.4, 58.3), Vector3(74.5, -3.8, 54.2)];
var locationIndex = 0;

function Start () {
relocate();


}

function Update () {

//if(Input.GetMouseButtonDown(0) || Cardboard.SDK.CardboardTriggered){
//relocate();
//}


}

function relocate(){
GetComponent.<Rigidbody>().position = areas[locationIndex];
locationIndex += 1;
if (locationIndex == areas.Length){locationIndex = 0;}
}