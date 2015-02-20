using UnityEngine;
using System.Collections;



public class location : MonoBehaviour {


	Vector3[] areas = new Vector3[3] {new Vector3(0,0,0), new Vector3(172, 17, 58), new Vector3(74, -4, 54)};
	int areaIndex = 0;
	Object cubes;
	public float speed = 3.0f;



	// Use this for initialization
	void Start () {
		relocate ();

	
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetMouseButtonDown (0) || Cardboard.SDK.CardboardTriggered || Input.GetKey(KeyCode.Return)) {
			relocate();
				}

		if (Input.GetKey (KeyCode.Space)) {
			transform.Translate(Vector3.up * Time.deltaTime*speed);

		}

		if (Input.GetKey (KeyCode.LeftShift) || Input.GetKey (KeyCode.RightShift)) {
						transform.Translate (Vector3.up * -Time.deltaTime * speed);
				}







		
	}
	
	void relocate(){
		transform.position = areas [areaIndex];
		areaIndex++;

		if (areaIndex == areas.Length) {areaIndex = 0;}

		}
}
