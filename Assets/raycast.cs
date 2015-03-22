using UnityEngine;
using System.Collections;

public class raycast : MonoBehaviour {
	private GameObject head;
	Color theColor = Color.black;
	private GameObject tag;

	string value = "";

	void Start () {
		head = GameObject.Find("CenterEyeAnchor");
		tag = GameObject.Find ("text");
		Debug.Log ("raycast enabled");
		theColor = GetComponent<Renderer>().material.color;
	}

	void Update () {
		Ray theGaze = new Ray(head.transform.position, head.transform.forward);
		Debug.DrawRay(head.transform.position, head.transform.forward*10, Color.white, 1.0f, true);
		RaycastHit hit;
		bool isLookedAt = GetComponent<Collider>().Raycast(theGaze, out hit, Mathf.Infinity);
		GetComponent<Renderer>().material.color = isLookedAt ? Color.green : theColor;
		if (isLookedAt) {
			tag.GetComponent<TextMesh>().text = value;
				}
	}

	void addValue(string val){
		value = value + val;
	}
}
