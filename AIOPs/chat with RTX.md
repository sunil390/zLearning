# Chat with RTX

## Install

1. Download from [here](https://www.nvidia.com/en-us/ai-on-rtx/chat-with-rtx-generative-ai/)
2. keep the default install folder (user name should not have spaces, there is a solution though)
3. customize for Shared access
```
cd C:\Users\zsuni\AppData\Local\NVIDIA\ChatWithRTX\RAG\trt-llm-rag-windows-main\ui

Edit user_interface.py and add share=Tue 
...
        interface.launch(
            favicon_path=os.path.join(os.path.dirname(__file__), 'assets/nvidia_logo.png'),
            show_api=False,share=True,
            server_port=port
        )
```
4. Permit proxy in Windows Defender

## Customize

1. Downloaded z/os 3.1 pdf files from [here](https://ibm-docs-static-content.s3.us.cloud-object-storage.appdomain.cloud/pdx/SSLTBW_3.1.0/zOS310-GA-Indexed-PDF-package-(2023-09-29).zip)
2. Change folder path to the unzipped folder where the pdf files are loaded.
3. retraining runs for 5 to 6 hours.
