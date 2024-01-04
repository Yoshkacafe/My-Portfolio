using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;
using TMPro;

public class linkSliderToText : MonoBehaviour
{
    public Slider sliderToLink;
    public TMP_Text textToLink;

    void Update()
    {
        textToLink.text = sliderToLink.value.ToString();
    }
}
