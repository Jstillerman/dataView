using UnityEngine;
using System.Collections;

public class raycast : MonoBehaviour {
	private CardboardHead head;
	Color theColor = Color.black;
	private GameObject tag;

	string value = "";
	
	void Start () {
		head = Camera.main.GetComponent<StereoController>().Head;
		tag = GameObject.Find ("text");
		Debug.Log ("raycast enabled");
		theColor = GetComponent<Renderer>().material.color;
	}

	void Update () {
		RaycastHit hit;
		bool isLookedAt = GetComponent<Collider>().Raycast(head.Gaze, out hit, Mathf.Infinity);
		GetComponent<Renderer>().material.color = isLookedAt ? Color.green : theColor;
		if (isLookedAt) {
			tag.GetComponent<TextMesh>().text = value;
				}
	}

	void addValue(string val){
		value = value + val;
	}
}
