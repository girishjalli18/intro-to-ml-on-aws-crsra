## Introduction to Machine Learning on AWS


### AWS documentation link for rekognition

https://docs.aws.amazon.com/code-library/latest/ug/python_3_rekognition_code_examples.html


### Getting started
-  Setup a AWS CLI

    install aws cli
    documentation link for AWS CLI
    https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

    download the cli tool

    ```
    curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
    sudo installer -pkg AWSCLIV2.pkg -target /
    ```

#### check for installation

`which aws`


### Set up the AWS CLI Profile

https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

# default profile
The config and credentials files are organized into sections named profiles

`aws configure`
    enter accessy key and secret key, region, output format


# named profile

`aws configure --profile <profile name>`


list, get, set aws configure
https://docs.aws.amazon.com/cli/latest/reference/configure/#:~:text=You%20can%20configure%20a%20named,when%20prompted%20for%20the%20value.


Optional:

### Github configuration

- setup git repo config

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

- check the config

```git config --list```

- check current config

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

- initialize the git repo

    cd to the working directory

    ``` git init ```