%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffe6f2'}}}%%
flowchart LR
    classDef structure fill:#99ff99,stroke:#009900
    classDef morphology fill:#ff9999,stroke:#ff0000
    classDef karyotype fill:#ffb366,stroke:#cc6600
    classDef abnormal fill:#ff99cc,stroke:#ff3399
    classDef special fill:#9999ff,stroke:#0000ff
    classDef analysis fill:#e6ccff,stroke:#6600cc

    %% Chromosome Structure
    A[Chromosomes] --> B{Structural Organization}
    class A structure
    class B structure

    B -->|Components| C[DNA + Histones]
    B -->|Packaging| D[Nucleosomes]
    B -->|Condensation| E[Chromatin Fiber]
    class C structure
    class D structure
    class E structure

    %% Morphology
    A --> F{Chromosome Morphology}
    class F morphology

    F -->|Position| G[Metacentric]
    F -->|Position| H[Submetacentric]
    F -->|Position| I[Acrocentric]
    F -->|Position| J[Telocentric]
    class G morphology
    class H morphology
    class I morphology
    class J morphology

    %% Karyotype Analysis
    A --> K{Karyotype Analysis}
    class K karyotype

    K -->|Normal| L[46,XX Female]
    K -->|Normal| M[46,XY Male]
    class L karyotype
    class M karyotype

    %% Abnormalities
    K -->|Numerical| N[Aneuploidies]
    class N abnormal

    N -->|Trisomy| O[Down Syndrome 47,XX+21]
    N -->|Monosomy| P[Turner Syndrome 45,X]
    N -->|Extra Sex| Q[Klinefelter 47,XXY]
    class O abnormal
    class P abnormal
    class Q abnormal

    %% Special Types
    A --> R{Special Chromosomes}
    class R special

    R -->|Sex| S[X Chromosome]
    R -->|Sex| T[Y Chromosome]
    R -->|Special| U[B Chromosomes]
    R -->|Modified| V[Polytene]
    class S special
    class T special
    class U special
    class V special

    %% Analysis Methods
    A --> W{Analysis Techniques}
    class W analysis

    W -->|Banding| X[G-Banding]
    W -->|FISH| Y[Fluorescence Methods]
    W -->|Modern| Z[Molecular Karyotyping]
    class X analysis
    class Y analysis
    class Z analysis

    subgraph Legend
        L1[Structural Elements]:::structure
        L2[Morphological Types]:::morphology
        L3[Normal Karyotypes]:::karyotype
        L4[Abnormalities]:::abnormal
        L5[Special Types]:::special
        L6[Analysis Methods]:::analysis
    end