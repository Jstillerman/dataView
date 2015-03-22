using UnityEngine;
using System.Collections;

public class centereyehack : MonoBehaviour {
	public GameObject head;
	// Use this for initialization
	void Start () {


	}

	// Update is called once per frame
	void Update () {
		Debug.Log("poopladoo");
		head.transform.rotation = transform.rotation;
		transform.rotation = new UnityEngine.Quaternion(0,0,0,0);

	}
}
