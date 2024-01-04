using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class BasicSettings : MonoBehaviour
{
    public Image exemple;
    public Image Background;
    public Image Fill;
    public Image Pause;
    public Image Jump;
    public Image Dash;
    public Image Panel;
    public Image Attack1;
    public Image Joystick;
    public Image Handle;
    public Slider opacitySlider;

    void Start()
    {
        exemple.GetComponent<Image>();
        Background.GetComponent<Image>();
        Fill.GetComponent<Image>();
        Pause.GetComponent<Image>();
        Jump.GetComponent<Image>();
        Dash.GetComponent<Image>();
        Panel.GetComponent<Image>();
        Attack1.GetComponent<Image>();
        Joystick.GetComponent<Image>();
        Handle.GetComponent<Image>();
    }

    void Update()
    {
        if (opacitySlider.value == 4)
        {
            exemple.color = new Color(exemple.color.r, exemple.color.g, exemple.color.b, 1f);
            Background.color = new Color(Background.color.r, Background.color.g, Background.color.b, 1f);
            Fill.color = new Color(Fill.color.r, Fill.color.g, Fill.color.b, 1f);
            Pause.color = new Color(Pause.color.r, Pause.color.g, Pause.color.b, 1f);
            Jump.color = new Color(Jump.color.r, Jump.color.g, Jump.color.b, 1f);
            Dash.color = new Color(Dash.color.r, Dash.color.g, Dash.color.b, 1f);
            Panel.color = new Color(Panel.color.r, Panel.color.g, Panel.color.b, 1f);
            Attack1.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, 1f);
            Joystick.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, 1f);
            Handle.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, 1f);
        } else if (opacitySlider.value == 3)
        {
            exemple.color = new Color(exemple.color.r, exemple.color.g, exemple.color.b, .85f);
            Background.color = new Color(Background.color.r, Background.color.g, Background.color.b, .85f);
            Fill.color = new Color(Fill.color.r, Fill.color.g, Fill.color.b, .85f);
            Pause.color = new Color(Pause.color.r, Pause.color.g, Pause.color.b, .85f);
            Jump.color = new Color(Jump.color.r, Jump.color.g, Jump.color.b, .85f);
            Dash.color = new Color(Dash.color.r, Dash.color.g, Dash.color.b, .85f);
            Panel.color = new Color(Panel.color.r, Panel.color.g, Panel.color.b, .85f);
            Attack1.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .85f);
            Joystick.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .85f);
            Handle.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .85f);
        } else if (opacitySlider.value == 2)
        {
            exemple.color = new Color(exemple.color.r, exemple.color.g, exemple.color.b, .75f);
            Background.color = new Color(Background.color.r, Background.color.g, Background.color.b, .75f);
            Fill.color = new Color(Fill.color.r, Fill.color.g, Fill.color.b, .75f);
            Pause.color = new Color(Pause.color.r, Pause.color.g, Pause.color.b, .75f);
            Jump.color = new Color(Jump.color.r, Jump.color.g, Jump.color.b, .75f);
            Dash.color = new Color(Dash.color.r, Dash.color.g, Dash.color.b, .75f);
            Panel.color = new Color(Panel.color.r, Panel.color.g, Panel.color.b, .75f);
            Attack1.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .75f);
            Joystick.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .75f);
            Handle.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .75f);
        } else if (opacitySlider.value == 1)
        {
            exemple.color = new Color(exemple.color.r, exemple.color.g, exemple.color.b, .5f);
            Background.color = new Color(Background.color.r, Background.color.g, Background.color.b, .5f);
            Fill.color = new Color(Fill.color.r, Fill.color.g, Fill.color.b, .5f);
            Pause.color = new Color(Pause.color.r, Pause.color.g, Pause.color.b, .5f);
            Jump.color = new Color(Jump.color.r, Jump.color.g, Jump.color.b, .5f);
            Dash.color = new Color(Dash.color.r, Dash.color.g, Dash.color.b, .5f);
            Panel.color = new Color(Panel.color.r, Panel.color.g, Panel.color.b, .5f);
            Attack1.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .5f);
            Joystick.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .5f);
            Handle.color = new Color(Attack1.color.r, Attack1.color.g, Attack1.color.b, .5f);
        } 
    }
}
