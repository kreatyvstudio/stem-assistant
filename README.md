<!-- README created using Best-README-Template https://github.com/othneildrew/Best-README-Template -->
<div>
  <h3>Curio the Cat: A Supportive AI Tutor for Elementary School STEM Subjects</h3>
  <p>Team Kreatyv Studio (Yelena V. Kozlova)<br>
  Women Who Code Hackathon for Social Good 2023</p>
</div>

> [!IMPORTANT]  
> OpenAI API key is required to run this application locally. See instructions below.

1. Head to [platform.openai.com/signup](https://platform.openai.com/signup) and create a free account. If you already have an OpenAI account, simply log in. **Note:** OpenAI is offering free API keys with $5 worth of free credit for the first three months. After the free credit is exhausted, payment information is required for API access.
2. Next, click on your profile in the top-right corner and select **View API keys** from the drop-down menu.
3. Click on “Create new secret key” and copy the API key.
4. Enter your Open AI API key in `config.py`

   ``` Python
   openai_api_key = "your-key-goes-here"
   ```

<!-- ABOUT THE PROJECT -->
## About The Project

### Challenge Statement

Despite the growing importance of STEM subjects, many young students, particularly girls, lack access to supportive and approachable guidance and mentorship, leading to a gap in STEM engagement and understanding. How can we make STEM subjects more approachable and less intimidating for these students?

### Proposed Solution

Curio, the Cat is a virtual AI assistant designed to be a friendly and supportive tutor for elementary school kids to support their learning of STEM subjects.
* Curio is a friendly virtual character that kids can chat with to ask questions and discuss STEM topics.
* The Curio chat app is powered by Open AI’s API and configured to have a friendly personality that uses appropriate language for school-age children, is provided constraints to only discuss STEM topics, and, like a tutor, walks the user through the process of a solution instead of providing direct answers.

### Project Demo and Presentation
Link to video of Project Demo: [Demo Video Link](https://drive.google.com/file/d/1U8LB_XDIdXWcGbmRijp8IglueZkk1xeo/view?usp=sharing)

Link to PDF of Project Overview: [PDF Link](https://drive.google.com/file/d/1odmygmC7yS1-v5PstjdTvrmtQbXhdg7R/view?usp=sharing)

### OpenAI API Configuration Playground
Playground link to view and test API configuration: https://platform.openai.com/playground/p/U15lYr38zoK51rXIue3u8jOa?model=gpt-3.5-turbo


### Built With

 [![Python][Python]][Python-url] 


### Installation
1. Clone the repo:

   ```sh
   git clone https://github.com/kreatyvstudio/stem-assistant.git
   ```
2. Check that the latest versions of Python and pip are installed in your environment.
3. Install OpenAI and Gradio Libraries. In the Terminal, run the below commands:

   ```sh
   pip3 install openai
   ```
   ```sh
   pip3 install gradio
   ```
4. Get OpenAI API Key at [platform.openai.com/signup](https://platform.openai.com/signup)
5. Enter your Open API Key in `config.py`

   ``` Python
   openai_api_key = "your-key-goes-here"
   ```
6. Copy the path to the location where you saved `assistant_app.py` and run the following command in Terminal:

   ```sh
   python3 insert-your-path-to-assistant_app.py
   ```
7. It outputs local URL, for example: http://127.0.0.1:7860, to open the app in any browser.


<!-- CONTACT -->
## Contact

Yelena V. Kozlova - [Linkedin](https://www.linkedin.com/in/yvkozlova/)

Project Link: [https://github.com/kreatyvstudio/stem-assistant](https://github.com/kreatyvstudio/stem-assistant)




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [Train ChatGPT with custom data and create your own chat bot using MacOS](https://medium.com/@sohaibshaheen/train-chatgpt-with-custom-data-and-create-your-own-chat-bot-using-macos-fb78c2f9646d)
* [How to Build Your Own AI Chatbot With ChatGPT API: A Step-by-Step Tutorial](https://beebom.com/how-build-own-ai-chatbot-with-chatgpt-api/)
* [How to Create a Custom Chatbot with Gradio Blocks](https://www.gradio.app/guides/creating-a-custom-chatbot-with-blocks)
* [3D Model](https://sketchfab.com/3d-models/vrc-quest-1a2ee6f7a86b4c09a2541614ea6e4ff5) by usaneko7256 is licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/)
* [Prompt Engineering Guide](https://www.promptingguide.ai/)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/curio_app_screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/