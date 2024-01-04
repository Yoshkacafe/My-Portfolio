using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SectionToucheSet : MonoBehaviour
{
    public Transform sword;
    public Transform dash;
    public Transform jump;

    public Vector3 swordVector;
    public Vector3 dashVector;
    public Vector3 jumpVector;

    public void Toggle1Action()
    {
        sword.transform.position = swordVector;
    }

    public void Toggle2Action()
    {
        dash.transform.position = dashVector;
    }

    public void Toggle3Action()
    {
        jump.transform.position = jumpVector;
    }

    public void ResetToggle1()
    {
        sword.transform.position = new Vector3(1432, 220, 0);
    }

    public void ResetToggle2()
    {
        dash.transform.position = new Vector3(1779, 218, 0);
    }

    public void ResetToggle3()
    {
        jump.transform.position = new Vector3(2103, 239, 0);
    }

}
