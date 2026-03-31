application:
  targetRevision: 
  server: <destination-cluster>
  name: <application-cluster>
  project: <application-project>
  labels:
    <labels for applications>
  annotations:
    <annotations for applications>
  revisionHistoryLimit: 1 # https://doc.crds.dev/github.com/argoproj/argo-cd/argoproj.io/Application/v1alpha1@v3.2.5#spec-ignoreDifferences
  ignoreDifferences: [] # https://doc.crds.dev/github.com/argoproj/argo-cd/argoproj.io/Application/v1alpha1@v3.2.5#spec-ignoreDifferences
  info: [] # https://doc.crds.dev/github.com/argoproj/argo-cd/argoproj.io/Application/v1alpha1@v3.2.5#spec-info
  sourceHydrator: {} # https://doc.crds.dev/github.com/argoproj/argo-cd/argoproj.io/Application/v1alpha1@v3.2.5#spec-sourceHydrator
  syncPolicy: {} # https://doc.crds.dev/github.com/argoproj/argo-cd/argoproj.io/Application/v1alpha1@v3.2.5#spec-syncPolicy

sources:
- # https://doc.crds.dev/github.com/argoproj/argo-cd/argoproj.io/Application/v1alpha1@v3.2.5#spec-source
  repoURL: placeholder
  targetRevision: v0.0.0
  chart: cert-manager  

extra:
  enabled: true
  # https://doc.crds.dev/github.com/argoproj/argo-cd/argoproj.io/Application/v1alpha1@v3.2.5#spec-source
  kustomize:
    commonLabels:
      coucou: oui