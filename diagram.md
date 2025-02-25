```mermaid
graph TD;

  %% Data Sources
  A[Kaggle Wildfire Data] -->|CSV/API| B[Extract Wildfire Data];
  C[Zillow Housing/Rental Data] -->|CSV/Parquet| D[Extract Housing Data];
  E[US Census Data] -->|CSV/TXT| F[Extract Population Data];

  %% Extract Phase
  B --> G[Load into Pandas DataFrame];
  D --> H[Load into Pandas DataFrame];
  F --> I[Load into Pandas DataFrame];

  %% Transformation Phase
  G --> J[Clean & Filter Wildfire Data];
  H --> K[Clean & Format Housing Data];
  I --> L[Normalize & Aggregate Population Data];

  %% Data Mapping & Integration
  J --> M[Map Location Data & Assign Location ID];
  K --> M;
  L --> M;

  %% Load Phase
  M -->|Final Processed Data| N[Store in Azure MySQL];

  %% Orchestration & Scheduling
  O[Scheduled Monthly Trigger] --> P[Cron Job / Airflow];
  P --> B;
  P --> D;
  P --> F;

  %% Data Consumers
  N -->|SQL Queries| Q[Business Intelligence / Dashboards];
  N -->|API Access| R[Real Estate Risk Applications];
  N -->|Exports| S[CSV/Parquet Reports];

  %% Labels
  classDef source fill:#FFDD57,stroke:#000,stroke-width:2px;
  classDef process fill:#87CEEB,stroke:#000,stroke-width:2px;
  classDef storage fill:#32CD32,stroke:#000,stroke-width:2px;
  classDef consumer fill:#FFA07A,stroke:#000,stroke-width:2px;
  classDef orchestration fill:#DDA0DD,stroke:#000,stroke-width:2px;

  class A,C,E source;
  class B,D,F,G,H,I,J,K,L process;
  class M,N storage;
  class Q,R,S consumer;
  class O,P orchestration;
