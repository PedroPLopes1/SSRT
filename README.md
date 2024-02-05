# Screen Space Ray Tracing
The SSRT (Screen Space Ray Tracing) shader is a custom shader for the Eevee render engine in Blender. It simulates light bouncing using screen space data, allowing for more realistic reflections and lighting in real-time.

## Installation
To use the SSRT shader and addon in Blender, follow these steps:

1. **Launch Blender:**
   - Open Blender on your system.

2. **Download SSRT:**
   - Download the [latest SSRT version](https://github.com/PedroPLopes1/SSRT/releases).

4. **Append Shader in Blender:**
   - Navigate to the `File` menu.
   - Choose the `Append` option.
   - Choose one of the `BLEND` files provided in the demos from the `Shader` folder.
   - Access the `NodeTree` folder.
   - Locate and select the `Principled BSDF SSRT` node group.
   - Complete the process by clicking the `Append` button.

5. **Install Addon:**
   - Navigate to the `File` menu.
   - Choose the `Preferences` option.
   - Navigate to the `Add-ons` section.
   - Click on the `Install...` button and select the `Principled_BSDF_Replacer.py` file from the `Addon` folder.
   - After selecting the `Principled_BSDF_Replacer.py` file, click on the `Install Add-on` button.

6. **Enable Addon:**
   - Once installed, find and enable the Principled BSDF SSRT Replacer addon.

## Usage
The SSRT shader can be used to create more realistic reflections and lighting in real-time in Blender Eevee. It works by simulating light bouncing using screen space data, which allows for more accurate reflections and lighting than traditional methods.

To use the SSRT shader effectively, consider the following tips:
- Apply the SSRT shader to the desired objects in your scene by selecting them and assigning the Principled BSDF SSRT node group.
- Adjust the shader settings, such as roughness and metallic values, to achieve the desired appearance of your materials.
- Experiment with different lighting setups and environment maps to enhance the realism of your scene.
- Keep in mind that the SSRT shader relies on screen space data, so objects that are not visible on the screen might not contribute to the lighting and reflections accurately.

## Addon
The SSRT addon provides operators to automatically replace Principled BSDF shader nodes with the Principled BSDF SSRT node group in Blender materials.

To use the addon, first install it and append the Principled BSDF SSRT node group following the [installation steps](https://github.com/PedroPLopes1/SSRT?tab=readme-ov-file#installation). Once completed, you can access it from the `3D Viewport Sidebar` > `Principled BSDF SSRT Replacer panel`.

The addon contains two replacement operators:

|  Operator | Description |
| --- | --- |
| `Replace Nodes in Selected Objects` | Replaces Principled BSDF nodes with the SSRT shader in materials of selected objects. |
| `Replace Nodes in Entire Scene` | Replaces Principled BSDF nodes with the SSRT shader in all materials in the scene. |

This allows existing scenes to be easily converted to use the SSRT shader. The node connections and values are preserved during replacement.

## Contributing

Contributions to the SSRT shader and addon are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to submit a pull request.

## License
This project is licensed under the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.](https://creativecommons.org/publicdomain/zero/1.0/deed.en)

## Credits
The addon script were developed by the talented 3D artist Gabriel Saretti. Check out [his work on Instagram](https://www.instagram.com/gabriel.saretti/).

## Acknowledgments
Special thanks to the developers and contributors of Blender and the Eevee render engine for providing a powerful and flexible platform for real-time rendering.

## Additional Resources
For more information on using the SSRT shader and advanced rendering techniques in Blender, you may find the following resources helpful:
- [Blender Documentation](https://docs.blender.org/manual/en/latest/)
- [Blender Artists Community](https://blenderartists.org/)
- [Blender Stack Exchange](https://blender.stackexchange.com/)
