using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Audio;

public class SettingsMenu : MonoBehaviour
{
    public AudioMixer audioMixer; 
    public AudioMixer audioMixerForEffects; 

    public void SetVolume (float volume)
    {
        audioMixer.SetFloat("Master", volume);
    }

    public void SetVolumeEffects(float effects)
    {
        audioMixerForEffects.SetFloat("Effects", effects);
    }

    public void SetQuality(int qualityIndex)
    {
        QualitySettings.SetQualityLevel(qualityIndex);
    }
}
