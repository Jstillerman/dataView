using UnityEngine;
using System.Collections;

public class controls : MonoBehaviour {
	public float x = 0f;
	public float z = 0f;
	public float rotation = 0f;
	public float speed = 3f;
	private CardboardHead head;

	// Use this for initialization
	void Start () {
		head = Camera.main.GetComponent<StereoController>().Head;
		rotation = head.Gaze.direction.y;
	
	}
	
	// Update is called once per frame
	void Update () {




		x = Mathf.Sin (rotation);
		z = Mathf.Cos (rotation);

		if (Input.GetKey (KeyCode.W) || Input.GetKey (KeyCode.UpArrow)) {
			transform.parent.Translate (new Vector3 (x * Time.deltaTime*speed, 0, z * Time.deltaTime*speed));
		}
		if (Input.GetKey (KeyCode.S) || Input.GetKey (KeyCode.DownArrow)) {
			transform.parent.Translate (new Vector3 (-x * Time.deltaTime*speed, 0, -z * Time.deltaTime*speed));
		}
		if (Input.GetKey (KeyCode.D) || Input.GetKey (KeyCode.RightArrow)) {
			transform.parent.Translate (new Vector3 (z * Time.deltaTime*speed, 0, x * Time.deltaTime*speed));
		}
		if (Input.GetKey (KeyCode.A) || Input.GetKey (KeyCode.LeftArrow)) {
			transform.parent.Translate (new Vector3 (-z * Time.deltaTime*speed, 0, -x * Time.deltaTime*speed));
		}
	
	}
}
