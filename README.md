# Nuclio Debug
This action will attempt a model deployment using [`nuctl`](https://nuclio.io/docs/latest/tasks/deploying-functions/). This action will read `function.yaml` and `main.py` from root folder.

## Usage
In order use this action, you need to [checkout nested](https://github.com/actions/checkout#Checkout-multiple-repos-nested) this action with your model repository. 
```bash
.
├── action.yml
├── common # folder
├── find_error.py
├── README.md
│  
└── your-model # your model here
    ├── function.yaml
    ├── main.py
    └── model_loader.py
```

After that, you can use this action in order to deploy model with nuclio.

```yaml
name: CI Model

env:
  MODEL-NAME: yolov5
  REPO-MODEL-PATH: model # default = model

on:
  release:
    types: [released]

jobs:
  nuclio-debug:
    needs: [ build-docker ]
    name: Debug Model with Nuclio
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Nuclio Debug Repo
        uses: actions/checkout@v3
        with:
          repository: 'ruhyadi/nuclio-debug'
          ref: v1.0

      - name: Checkout Model Repo
        uses: actions/checkout@v3
        with:
          repository: ${{ github.repository }}
          path: ${{ env.REPO-MODEL-PATH }}

      - name: Deploy Model
        id: deploy-model
        uses: ruhyadi/nuclio-debug@v1.0
        with:
          model-path: ./${{ env.REPO-MODEL-PATH }}
          model-name: ${{ env.MODEL-NAME }}
```

---
Original implementation of this action can be refer to [Xu-Justin/nuctl-deploy-checker-action](https://github.com/Xu-Justin/nuctl-deploy-checker-action)

This project was developed as part of **Nodeflux Internship x Kampus Merdeka**.
