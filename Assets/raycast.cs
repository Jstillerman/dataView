using UnityEngine;
using System.Collections;

public class raycast : MonoBehaviour {
	private OVRCameraRig head;
	Color theColor = Color.black;
	private GameObject tag;
	Vector3 pos;
	GameObject dot;

	string value = "";
	
	void Start () {
		//head = Camera.main.GetComponent<StereoController>().Head;
		head = GameObject.Find ("OVRCameraRig").GetComponent<OVRCameraRig> ();
		tag = GameObject.Find ("text");
		dot = GameObject.Find ("Plane");

		Debug.Log ("raycast enabled");
		//Debug.DrawLine(, new Vector3(1, 0, 0), Color.red);
		theColor = renderer.material.color;
	}

	void Update () {
		RaycastHit hit;
		pos = dot.transform.position;
		bool isLookedAt = GetComponent<Collider>().Raycast(head.camera.ViewportPointToRay(pos), out hit, Mathf.Infinity);
		GetComponent<Renderer>().material.color = isLookedAt ? Color.green : theColor;
		if (isLookedAt) {
			tag.GetComponent<TextMesh>().text = value;
				}
	}

	void addValue(string val){
		value = value + val;
	}
}
