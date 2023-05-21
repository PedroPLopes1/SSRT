# Screen Space Ray Tracing
The SSRT (Screen Space Ray Tracing) shader is a custom shader for the Eevee render engine in Blender. It simulates light bouncing using screen space data, allowing for more realistic reflections and lighting in real-time.

## Installation
To use the SSRT shader in Blender Eevee, follow these steps:

1. Launch Blender and initiate a new project.
2. Proceed to the "File" menu and choose the "Append" option.
2. Choose one of the .blend files provided in this [link](https://github.com/PedroPLopes1/SSRT/tree/main/Shader).
3. Inside the file browser, open the "NodeTree" directory.
4. Identify the "Principled BSDF SSRT" option and select it.
5. Finalize the process by clicking the "Append" button.

## Usage
The SSRT shader can be used to create more realistic reflections and lighting in real-time in Blender Eevee. It works by simulating light bouncing using screen space data, which allows for more accurate reflections and lighting than traditional methods.

To use the SSRT shader effectively, consider the following tips:
- Apply the SSRT shader to the desired objects in your scene by selecting them and assigning the "Principled BSDF SSRT" node group.
- Adjust the shader settings, such as roughness and metallic values, to achieve the desired appearance of your materials.
- Experiment with different lighting setups and environment maps to enhance the realism of your scene.
- Keep in mind that the SSRT shader relies on screen space data, so objects that are not visible on the screen might not contribute to the lighting and reflections accurately.

## Contributing
Contributions to the SSRT shader are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to submit a pull request.

## License
This project is licensed under the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.](https://creativecommons.org/publicdomain/zero/1.0/deed.en)

## Acknowledgments
Special thanks to the developers and contributors of [Blender](https://www.blender.org/) and the Eevee render engine for providing a powerful and flexible platform for real-time rendering.

## Additional Resources
For more information on using the SSRT shader and advanced rendering techniques in Blender, you may find the following resources helpful:
- [Blender Documentation](https://docs.blender.org/manual/en/latest/)
- [Blender Artists Community](https://blenderartists.org/)
- [Blender Stack Exchange](https://blender.stackexchange.com/)
