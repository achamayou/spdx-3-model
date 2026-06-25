# CoSPDX integer mapping

This document summarizes the integer assignments in `cospdx.cddl` and how they relate to the SPDX 3.0.1 JSON-LD context. It was generated from:

- `https://github.com/achamayou/draft-chamayou-cospdx/blob/main/cospdx.cddl`
- `https://spdx.github.io/spdx-spec/v3.0.1/rdf/spdx-context.jsonld`

## Summary

The CDDL integer space is not limited to model properties. `label.*` entries are used for map keys, while `const.*` entries cover RDF/class terms, controlled-vocabulary terms, vocabulary values, profile aliases, and singleton values.

Total assignments: **725**.

| Category | Count | Meaning |
|---|---:|---|
| Model property | 160 | SPDX model properties encoded as `label.<property>` map keys. |
| JSON-LD structural key | 3 | JSON-LD syntax keys encoded as labels. |
| Object/class term | 55 | Concrete SPDX object or relationship classes encoded as `const.<class>` values. |
| Vocabulary/type class | 23 | Controlled-vocabulary classes such as `HashAlgorithm` or `RelationshipType`. |
| Fully-qualified vocabulary member | 254 | Canonical vocabulary values with `spdx_<Profile>_<Type>_<value>` names. |
| Local vocabulary member alias | 216 | Short aliases for vocabulary values used in compact property values. |
| Profile/namespace alias | 9 | Profile identifiers used in profile conformance values. |
| Special singleton term | 5 | Singleton/non-object constants such as `NoneElement` or `NoAssertionElement`. |

## Context terms without integer assignments

The following top-level JSON-LD context terms do not have a `const.` or `label.` integer assignment in the CDDL. They are mainly abstract/base terms or namespace roots.

| Term | JSON-LD value |
|---|---|
| `Artifact` | `https://spdx.org/rdf/3.0.1/terms/Core/Artifact` |
| `Element` | `https://spdx.org/rdf/3.0.1/terms/Core/Element` |
| `ElementCollection` | `https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection` |
| `IntegrityMethod` | `https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod` |
| `expandedlicensing_ExtendableLicense` | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense` |
| `expandedlicensing_License` | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License` |
| `expandedlicensing_LicenseAddition` | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition` |
| `extension_Extension` | `https://spdx.org/rdf/3.0.1/terms/Extension/Extension` |
| `security_VexVulnAssessmentRelationship` | `https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship` |
| `security_VulnAssessmentRelationship` | `https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship` |
| `simplelicensing_AnyLicenseInfo` | `https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo` |
| `software_SoftwareArtifact` | `https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact` |
| `spdx` | `https://spdx.org/rdf/3.0.1/terms/` |

## Complete integer mapping

| Integer | CDDL name | Category | Source | JSON-LD/model URL | CDDL line |
|---:|---|---|---|---|---:|
| 1 | `label.@graph` | JSON-LD structural key | CDDL-only or derived alias | `` | 642 |
| 2 | `label.type` | JSON-LD structural key | JSON-LD string term | `@type` | 643 |
| 3 | `label.@id` | JSON-LD structural key | CDDL-only or derived alias | `` | 644 |
| 4 | `label.software_contentIdentifierType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifierType/` | 646 |
| 5 | `label.software_contentIdentifierValue` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifierValue/` | 648 |
| 6 | `label.software_additionalPurpose` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/additionalPurpose/` | 650 |
| 7 | `label.software_attributionText` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/attributionText/` | 652 |
| 8 | `label.software_contentIdentifier` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifier/` | 654 |
| 9 | `label.software_copyrightText` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/copyrightText/` | 656 |
| 10 | `label.software_primaryPurpose` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/primaryPurpose/` | 658 |
| 11 | `label.spdxId` | Model property | JSON-LD string term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/spdxId/` | 660 |
| 12 | `label.contentType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/contentType/` | 662 |
| 13 | `label.software_fileKind` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/fileKind/` | 664 |
| 14 | `label.software_downloadLocation` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/downloadLocation/` | 666 |
| 15 | `label.software_homePage` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/homePage/` | 668 |
| 16 | `label.software_packageUrl` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageUrl/` | 670 |
| 17 | `label.software_packageVersion` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageVersion/` | 672 |
| 18 | `label.software_sourceInfo` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/sourceInfo/` | 674 |
| 19 | `label.software_sbomType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/sbomType/` | 676 |
| 20 | `label.software_byteRange` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/byteRange/` | 678 |
| 21 | `label.software_lineRange` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/lineRange/` | 680 |
| 22 | `label.software_snippetFromFile` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/snippetFromFile/` | 682 |
| 23 | `label.suppliedBy` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/` | 684 |
| 24 | `label.security_assessedElement` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/` | 686 |
| 25 | `label.security_modifiedTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/` | 688 |
| 26 | `label.security_publishedTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/` | 690 |
| 27 | `label.security_withdrawnTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/` | 692 |
| 28 | `label.security_score` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/score/` | 694 |
| 29 | `label.security_vectorString` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vectorString/` | 696 |
| 30 | `label.security_severity` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/severity/` | 698 |
| 31 | `label.security_percentile` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/percentile/` | 700 |
| 32 | `label.security_probability` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/probability/` | 702 |
| 33 | `label.security_catalogType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/catalogType/` | 704 |
| 34 | `label.security_exploited` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/exploited/` | 706 |
| 35 | `label.security_locator` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/locator/` | 708 |
| 36 | `label.security_decisionType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/decisionType/` | 710 |
| 37 | `label.security_statusNotes` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/statusNotes/` | 712 |
| 38 | `label.security_vexVersion` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vexVersion/` | 714 |
| 39 | `label.security_actionStatement` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/actionStatement/` | 716 |
| 40 | `label.security_actionStatementTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/actionStatementTime/` | 718 |
| 41 | `label.security_impactStatement` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/impactStatement/` | 720 |
| 42 | `label.security_impactStatementTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/impactStatementTime/` | 722 |
| 43 | `label.security_justificationType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/justificationType/` | 724 |
| 44 | `label.simplelicensing_customIdToUri` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/customIdToUri/` | 726 |
| 45 | `label.simplelicensing_licenseExpression` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseExpression/` | 728 |
| 46 | `label.simplelicensing_licenseListVersion` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseListVersion/` | 730 |
| 47 | `label.simplelicensing_licenseText` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseText/` | 732 |
| 48 | `label.expandedlicensing_additionText` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/additionText/` | 734 |
| 49 | `label.expandedlicensing_isDeprecatedAdditionId` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isDeprecatedAdditionId/` | 736 |
| 50 | `label.expandedlicensing_licenseXml` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/licenseXml/` | 738 |
| 51 | `label.expandedlicensing_obsoletedBy` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/obsoletedBy/` | 740 |
| 52 | `label.expandedlicensing_seeAlso` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/seeAlso/` | 742 |
| 53 | `label.expandedlicensing_standardAdditionTemplate` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardAdditionTemplate/` | 744 |
| 54 | `label.expandedlicensing_deprecatedVersion` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/deprecatedVersion/` | 746 |
| 55 | `label.expandedlicensing_listVersionAdded` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/listVersionAdded/` | 748 |
| 56 | `label.expandedlicensing_member` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/member/` | 750 |
| 57 | `label.expandedlicensing_isDeprecatedLicenseId` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isDeprecatedLicenseId/` | 752 |
| 58 | `label.expandedlicensing_isFsfLibre` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isFsfLibre/` | 754 |
| 59 | `label.expandedlicensing_isOsiApproved` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isOsiApproved/` | 756 |
| 60 | `label.expandedlicensing_standardLicenseHeader` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardLicenseHeader/` | 758 |
| 61 | `label.expandedlicensing_standardLicenseTemplate` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardLicenseTemplate/` | 760 |
| 62 | `label.expandedlicensing_subjectLicense` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/subjectLicense/` | 762 |
| 63 | `label.expandedlicensing_subjectAddition` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/subjectAddition/` | 764 |
| 64 | `label.expandedlicensing_subjectExtendableLicense` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/subjectExtendableLicense/` | 766 |
| 65 | `label.dataset_anonymizationMethodUsed` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/anonymizationMethodUsed/` | 768 |
| 66 | `label.dataset_confidentialityLevel` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/confidentialityLevel/` | 770 |
| 67 | `label.dataset_dataCollectionProcess` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/dataCollectionProcess/` | 772 |
| 68 | `label.dataset_dataPreprocessing` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/dataPreprocessing/` | 774 |
| 69 | `label.dataset_datasetAvailability` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetAvailability/` | 776 |
| 70 | `label.dataset_datasetNoise` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetNoise/` | 778 |
| 71 | `label.dataset_datasetSize` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetSize/` | 780 |
| 72 | `label.dataset_datasetType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetType/` | 782 |
| 73 | `label.dataset_datasetUpdateMechanism` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetUpdateMechanism/` | 784 |
| 74 | `label.dataset_hasSensitivePersonalInformation` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/hasSensitivePersonalInformation/` | 786 |
| 75 | `label.dataset_intendedUse` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/intendedUse/` | 788 |
| 76 | `label.dataset_knownBias` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/knownBias/` | 790 |
| 77 | `label.dataset_sensor` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/sensor/` | 792 |
| 78 | `label.ai_finetuningEnergyConsumption` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/finetuningEnergyConsumption/` | 794 |
| 79 | `label.ai_inferenceEnergyConsumption` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/inferenceEnergyConsumption/` | 796 |
| 80 | `label.ai_trainingEnergyConsumption` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/trainingEnergyConsumption/` | 798 |
| 81 | `label.ai_energyQuantity` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/energyQuantity/` | 800 |
| 82 | `label.ai_energyUnit` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/energyUnit/` | 802 |
| 83 | `label.ai_autonomyType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/autonomyType/` | 804 |
| 84 | `label.ai_domain` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/domain/` | 806 |
| 85 | `label.ai_energyConsumption` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/energyConsumption/` | 808 |
| 86 | `label.ai_hyperparameter` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/hyperparameter/` | 810 |
| 87 | `label.ai_informationAboutApplication` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/informationAboutApplication/` | 812 |
| 88 | `label.ai_informationAboutTraining` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/informationAboutTraining/` | 814 |
| 89 | `label.ai_limitation` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/limitation/` | 816 |
| 90 | `label.ai_metric` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/metric/` | 818 |
| 91 | `label.ai_metricDecisionThreshold` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/metricDecisionThreshold/` | 820 |
| 92 | `label.ai_modelDataPreprocessing` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/modelDataPreprocessing/` | 822 |
| 93 | `label.ai_modelExplainability` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/modelExplainability/` | 824 |
| 94 | `label.ai_safetyRiskAssessment` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/safetyRiskAssessment/` | 826 |
| 95 | `label.ai_standardCompliance` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/standardCompliance/` | 828 |
| 96 | `label.ai_typeOfModel` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/typeOfModel/` | 830 |
| 97 | `label.ai_useSensitivePersonalInformation` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/useSensitivePersonalInformation/` | 832 |
| 98 | `label.build_buildEndTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/buildEndTime/` | 834 |
| 99 | `label.build_buildId` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/buildId/` | 836 |
| 100 | `label.build_buildStartTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/buildStartTime/` | 838 |
| 101 | `label.build_buildType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/buildType/` | 840 |
| 102 | `label.build_configSourceDigest` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/configSourceDigest/` | 842 |
| 103 | `label.build_configSourceEntrypoint` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/configSourceEntrypoint/` | 844 |
| 104 | `label.build_configSourceUri` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/configSourceUri/` | 846 |
| 105 | `label.build_environment` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/environment/` | 848 |
| 106 | `label.build_parameter` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/parameter/` | 850 |
| 107 | `label.extension_cdxPropName` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Properties/cdxPropName/` | 852 |
| 108 | `label.extension_cdxPropValue` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Properties/cdxPropValue/` | 854 |
| 109 | `label.extension_cdxProperty` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Properties/cdxProperty/` | 856 |
| 110 | `label.comment` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/` | 858 |
| 111 | `label.created` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/created/` | 860 |
| 112 | `label.createdBy` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/createdBy/` | 862 |
| 113 | `label.createdUsing` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/createdUsing/` | 864 |
| 114 | `label.specVersion` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/specVersion/` | 866 |
| 115 | `label.key` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/key/` | 868 |
| 116 | `label.value` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/value/` | 870 |
| 117 | `label.creationInfo` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/` | 872 |
| 118 | `label.description` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/` | 874 |
| 119 | `label.extension` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/` | 876 |
| 120 | `label.externalIdentifier` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/` | 878 |
| 121 | `label.externalRef` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/` | 880 |
| 122 | `label.name` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/` | 882 |
| 123 | `label.summary` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/` | 884 |
| 124 | `label.verifiedUsing` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/` | 886 |
| 125 | `label.element` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/element/` | 888 |
| 126 | `label.profileConformance` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/profileConformance/` | 890 |
| 127 | `label.rootElement` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/rootElement/` | 892 |
| 128 | `label.externalIdentifierType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifierType/` | 894 |
| 129 | `label.identifier` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/identifier/` | 896 |
| 130 | `label.identifierLocator` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/identifierLocator/` | 898 |
| 131 | `label.issuingAuthority` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/issuingAuthority/` | 900 |
| 132 | `label.definingArtifact` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/definingArtifact/` | 902 |
| 133 | `label.externalSpdxId` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalSpdxId/` | 904 |
| 134 | `label.locationHint` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/locationHint/` | 906 |
| 135 | `label.externalRefType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRefType/` | 908 |
| 136 | `label.locator` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/locator/` | 910 |
| 137 | `label.namespace` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/namespace/` | 912 |
| 138 | `label.prefix` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/prefix/` | 914 |
| 139 | `label.algorithm` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/algorithm/` | 916 |
| 140 | `label.hashValue` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/hashValue/` | 918 |
| 141 | `label.packageVerificationCodeExcludedFile` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/packageVerificationCodeExcludedFile/` | 920 |
| 142 | `label.beginIntegerRange` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/beginIntegerRange/` | 922 |
| 143 | `label.endIntegerRange` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endIntegerRange/` | 924 |
| 144 | `label.completeness` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/` | 926 |
| 145 | `label.endTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/` | 928 |
| 146 | `label.from` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/` | 930 |
| 147 | `label.relationshipType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/` | 932 |
| 148 | `label.startTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/` | 934 |
| 149 | `label.to` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/` | 936 |
| 150 | `label.dataLicense` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/dataLicense/` | 938 |
| 151 | `label.import` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/import/` | 940 |
| 152 | `label.namespaceMap` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/namespaceMap/` | 942 |
| 153 | `label.annotationType` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/annotationType/` | 944 |
| 154 | `label.statement` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/statement/` | 946 |
| 155 | `label.subject` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/subject/` | 948 |
| 156 | `label.builtTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/` | 950 |
| 157 | `label.originatedBy` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/` | 952 |
| 158 | `label.releaseTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/` | 954 |
| 159 | `label.standardName` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/` | 956 |
| 160 | `label.supportLevel` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/` | 958 |
| 161 | `label.validUntilTime` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/` | 960 |
| 162 | `label.context` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/context/` | 962 |
| 163 | `label.scope` | Model property | JSON-LD object term | `https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/scope/` | 964 |
| 1001 | `const.software_ContentIdentifier` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifier` | 967 |
| 1002 | `const.gitoid` | Local vocabulary member alias | CDDL-only or derived alias | `` | 968 |
| 1003 | `const.swhid` | Local vocabulary member alias | CDDL-only or derived alias | `` | 969 |
| 1004 | `const.software_ContentIdentifierType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType` | 970 |
| 1005 | `const.spdx_Software_ContentIdentifierType_gitoid` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 971 |
| 1006 | `const.spdx_Software_ContentIdentifierType_swhid` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 972 |
| 1007 | `const.software_FileKindType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/FileKindType` | 973 |
| 1008 | `const.spdx_Software_FileKindType_directory` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 974 |
| 1009 | `const.spdx_Software_FileKindType_file` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 975 |
| 1010 | `const.software_SbomType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/SbomType` | 976 |
| 1011 | `const.spdx_Software_SbomType_analyzed` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 977 |
| 1012 | `const.spdx_Software_SbomType_build` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 978 |
| 1013 | `const.spdx_Software_SbomType_deployed` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 979 |
| 1014 | `const.spdx_Software_SbomType_design` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 980 |
| 1015 | `const.spdx_Software_SbomType_runtime` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 981 |
| 1016 | `const.spdx_Software_SbomType_source` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 982 |
| 1017 | `const.software_SoftwarePurpose` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose` | 983 |
| 1018 | `const.spdx_Software_SoftwarePurpose_application` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 984 |
| 1019 | `const.spdx_Software_SoftwarePurpose_archive` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 985 |
| 1020 | `const.spdx_Software_SoftwarePurpose_bom` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 986 |
| 1021 | `const.spdx_Software_SoftwarePurpose_configuration` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 987 |
| 1022 | `const.spdx_Software_SoftwarePurpose_container` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 988 |
| 1023 | `const.spdx_Software_SoftwarePurpose_data` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 989 |
| 1024 | `const.spdx_Software_SoftwarePurpose_device` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 990 |
| 1025 | `const.spdx_Software_SoftwarePurpose_deviceDriver` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 991 |
| 1026 | `const.spdx_Software_SoftwarePurpose_diskImage` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 992 |
| 1027 | `const.spdx_Software_SoftwarePurpose_documentation` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 993 |
| 1028 | `const.spdx_Software_SoftwarePurpose_evidence` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 994 |
| 1029 | `const.spdx_Software_SoftwarePurpose_executable` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 995 |
| 1030 | `const.spdx_Software_SoftwarePurpose_file` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 996 |
| 1031 | `const.spdx_Software_SoftwarePurpose_filesystemImage` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 997 |
| 1032 | `const.spdx_Software_SoftwarePurpose_firmware` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 998 |
| 1033 | `const.spdx_Software_SoftwarePurpose_framework` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 999 |
| 1034 | `const.spdx_Software_SoftwarePurpose_install` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1000 |
| 1035 | `const.spdx_Software_SoftwarePurpose_library` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1001 |
| 1036 | `const.spdx_Software_SoftwarePurpose_manifest` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1002 |
| 1037 | `const.spdx_Software_SoftwarePurpose_model` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1003 |
| 1038 | `const.spdx_Software_SoftwarePurpose_module` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1004 |
| 1039 | `const.spdx_Software_SoftwarePurpose_operatingSystem` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1005 |
| 1040 | `const.spdx_Software_SoftwarePurpose_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1006 |
| 1041 | `const.spdx_Software_SoftwarePurpose_patch` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1007 |
| 1042 | `const.spdx_Software_SoftwarePurpose_platform` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1008 |
| 1043 | `const.spdx_Software_SoftwarePurpose_requirement` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1009 |
| 1044 | `const.spdx_Software_SoftwarePurpose_source` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1010 |
| 1045 | `const.spdx_Software_SoftwarePurpose_specification` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1011 |
| 1046 | `const.spdx_Software_SoftwarePurpose_test` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1012 |
| 1047 | `const.application` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1013 |
| 1048 | `const.archive` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1014 |
| 1049 | `const.bom` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1015 |
| 1050 | `const.configuration` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1016 |
| 1051 | `const.container` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1017 |
| 1052 | `const.data` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1018 |
| 1053 | `const.device` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1019 |
| 1054 | `const.deviceDriver` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1020 |
| 1055 | `const.diskImage` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1021 |
| 1056 | `const.documentation` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1022 |
| 1057 | `const.evidence` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1023 |
| 1058 | `const.executable` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1024 |
| 1059 | `const.file` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1025 |
| 1060 | `const.filesystemImage` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1026 |
| 1061 | `const.firmware` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1027 |
| 1062 | `const.framework` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1028 |
| 1063 | `const.install` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1029 |
| 1064 | `const.library` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1030 |
| 1065 | `const.manifest` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1031 |
| 1066 | `const.model` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1032 |
| 1067 | `const.module` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1033 |
| 1068 | `const.operatingSystem` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1034 |
| 1069 | `const.other` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1035 |
| 1070 | `const.patch` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1036 |
| 1071 | `const.platform` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1037 |
| 1072 | `const.requirement` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1038 |
| 1073 | `const.source` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1039 |
| 1074 | `const.specification` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1040 |
| 1075 | `const.test` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1041 |
| 1076 | `const.software_File` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/File` | 1042 |
| 1077 | `const.directory` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1043 |
| 1078 | `const.software_Package` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/Package` | 1044 |
| 1079 | `const.software_Sbom` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/Sbom` | 1045 |
| 1080 | `const.analyzed` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1046 |
| 1081 | `const.build` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1047 |
| 1082 | `const.deployed` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1048 |
| 1083 | `const.design` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1049 |
| 1084 | `const.runtime` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1050 |
| 1085 | `const.software_Snippet` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Software/Snippet` | 1051 |
| 1086 | `const.security_CvssSeverityType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType` | 1052 |
| 1087 | `const.spdx_Security_CvssSeverityType_critical` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1053 |
| 1088 | `const.spdx_Security_CvssSeverityType_high` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1054 |
| 1089 | `const.spdx_Security_CvssSeverityType_low` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1055 |
| 1090 | `const.spdx_Security_CvssSeverityType_medium` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1056 |
| 1091 | `const.spdx_Security_CvssSeverityType_none` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1057 |
| 1092 | `const.security_ExploitCatalogType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType` | 1058 |
| 1093 | `const.spdx_Security_ExploitCatalogType_kev` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1059 |
| 1094 | `const.spdx_Security_ExploitCatalogType_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1060 |
| 1095 | `const.security_SsvcDecisionType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType` | 1061 |
| 1096 | `const.spdx_Security_SsvcDecisionType_act` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1062 |
| 1097 | `const.spdx_Security_SsvcDecisionType_attend` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1063 |
| 1098 | `const.spdx_Security_SsvcDecisionType_track` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1064 |
| 1099 | `const.spdx_Security_SsvcDecisionType_trackStar` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1065 |
| 1100 | `const.security_VexJustificationType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType` | 1066 |
| 1101 | `const.spdx_Security_VexJustificationType_componentNotPresent` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1067 |
| 1102 | `const.spdx_Security_VexJustificationType_inlineMitigationsAlreadyExist` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1068 |
| 1103 | `const.spdx_Security_VexJustificationType_vulnerableCodeCannotBeControlledByAdversary` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1069 |
| 1104 | `const.spdx_Security_VexJustificationType_vulnerableCodeNotInExecutePath` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1070 |
| 1105 | `const.spdx_Security_VexJustificationType_vulnerableCodeNotPresent` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1071 |
| 1106 | `const.security_CvssV2VulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/CvssV2VulnAssessmentRelationship` | 1072 |
| 1107 | `const.security_CvssV3VulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/CvssV3VulnAssessmentRelationship` | 1073 |
| 1108 | `const.critical` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1074 |
| 1109 | `const.high` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1075 |
| 1110 | `const.low` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1076 |
| 1111 | `const.medium` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1077 |
| 1112 | `const.none` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1078 |
| 1113 | `const.security_CvssV4VulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/CvssV4VulnAssessmentRelationship` | 1079 |
| 1114 | `const.security_EpssVulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/EpssVulnAssessmentRelationship` | 1080 |
| 1115 | `const.security_ExploitCatalogVulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogVulnAssessmentRelationship` | 1081 |
| 1116 | `const.kev` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1082 |
| 1117 | `const.security_SsvcVulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/SsvcVulnAssessmentRelationship` | 1083 |
| 1118 | `const.act` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1084 |
| 1119 | `const.attend` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1085 |
| 1120 | `const.track` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1086 |
| 1121 | `const.trackStar` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1087 |
| 1122 | `const.security_Vulnerability` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/Vulnerability` | 1088 |
| 1123 | `const.security_VexAffectedVulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/VexAffectedVulnAssessmentRelationship` | 1089 |
| 1124 | `const.security_VexFixedVulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/VexFixedVulnAssessmentRelationship` | 1090 |
| 1125 | `const.security_VexNotAffectedVulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/VexNotAffectedVulnAssessmentRelationship` | 1091 |
| 1126 | `const.componentNotPresent` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1092 |
| 1127 | `const.inlineMitigationsAlreadyExist` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1093 |
| 1128 | `const.vulnerableCodeCannotBeControlledByAdversary` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1094 |
| 1129 | `const.vulnerableCodeNotInExecutePath` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1095 |
| 1130 | `const.vulnerableCodeNotPresent` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1096 |
| 1131 | `const.security_VexUnderInvestigationVulnAssessmentRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Security/VexUnderInvestigationVulnAssessmentRelationship` | 1097 |
| 1132 | `const.expandedlicensing_NoAssertionLicense` | Special singleton term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoAssertionLicense` | 1098 |
| 1133 | `const.expandedlicensing_NoneLicense` | Special singleton term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoneLicense` | 1099 |
| 1134 | `const.simplelicensing_LicenseExpression` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/LicenseExpression` | 1100 |
| 1135 | `const.simplelicensing_SimpleLicensingText` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/SimpleLicensingText` | 1101 |
| 1136 | `const.expandedlicensing_ListedLicenseException` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicenseException` | 1102 |
| 1137 | `const.expandedlicensing_ConjunctiveLicenseSet` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ConjunctiveLicenseSet` | 1103 |
| 1138 | `const.expandedlicensing_CustomLicenseAddition` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicenseAddition` | 1104 |
| 1139 | `const.expandedlicensing_DisjunctiveLicenseSet` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/DisjunctiveLicenseSet` | 1105 |
| 1140 | `const.expandedlicensing_IndividualLicensingInfo` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/IndividualLicensingInfo` | 1106 |
| 1141 | `const.expandedlicensing_ListedLicense` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicense` | 1107 |
| 1142 | `const.expandedlicensing_OrLaterOperator` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/OrLaterOperator` | 1108 |
| 1143 | `const.expandedlicensing_WithAdditionOperator` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/WithAdditionOperator` | 1109 |
| 1144 | `const.expandedlicensing_CustomLicense` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicense` | 1110 |
| 1145 | `const.dataset_ConfidentialityLevelType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType` | 1111 |
| 1146 | `const.spdx_Dataset_ConfidentialityLevelType_amber` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1112 |
| 1147 | `const.spdx_Dataset_ConfidentialityLevelType_clear` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1113 |
| 1148 | `const.spdx_Dataset_ConfidentialityLevelType_green` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1114 |
| 1149 | `const.spdx_Dataset_ConfidentialityLevelType_red` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1115 |
| 1150 | `const.dataset_DatasetAvailabilityType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType` | 1116 |
| 1151 | `const.spdx_Dataset_DatasetAvailabilityType_clickthrough` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1117 |
| 1152 | `const.spdx_Dataset_DatasetAvailabilityType_directDownload` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1118 |
| 1153 | `const.spdx_Dataset_DatasetAvailabilityType_query` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1119 |
| 1154 | `const.spdx_Dataset_DatasetAvailabilityType_registration` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1120 |
| 1155 | `const.spdx_Dataset_DatasetAvailabilityType_scrapingScript` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1121 |
| 1156 | `const.dataset_DatasetType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType` | 1122 |
| 1157 | `const.spdx_Dataset_DatasetType_audio` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1123 |
| 1158 | `const.spdx_Dataset_DatasetType_categorical` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1124 |
| 1159 | `const.spdx_Dataset_DatasetType_graph` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1125 |
| 1160 | `const.spdx_Dataset_DatasetType_image` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1126 |
| 1161 | `const.spdx_Dataset_DatasetType_noAssertion` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1127 |
| 1162 | `const.spdx_Dataset_DatasetType_numeric` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1128 |
| 1163 | `const.spdx_Dataset_DatasetType_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1129 |
| 1164 | `const.spdx_Dataset_DatasetType_sensor` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1130 |
| 1165 | `const.spdx_Dataset_DatasetType_structured` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1131 |
| 1166 | `const.spdx_Dataset_DatasetType_syntactic` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1132 |
| 1167 | `const.spdx_Dataset_DatasetType_text` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1133 |
| 1168 | `const.spdx_Dataset_DatasetType_timeseries` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1134 |
| 1169 | `const.spdx_Dataset_DatasetType_timestamp` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1135 |
| 1170 | `const.spdx_Dataset_DatasetType_video` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1136 |
| 1171 | `const.dataset_DatasetPackage` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetPackage` | 1137 |
| 1172 | `const.amber` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1138 |
| 1173 | `const.clear` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1139 |
| 1174 | `const.green` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1140 |
| 1175 | `const.red` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1141 |
| 1176 | `const.clickthrough` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1142 |
| 1177 | `const.directDownload` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1143 |
| 1178 | `const.query` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1144 |
| 1179 | `const.registration` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1145 |
| 1180 | `const.scrapingScript` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1146 |
| 1181 | `const.audio` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1147 |
| 1182 | `const.categorical` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1148 |
| 1183 | `const.graph` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1149 |
| 1184 | `const.image` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1150 |
| 1185 | `const.noAssertion` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1151 |
| 1186 | `const.numeric` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1152 |
| 1187 | `const.sensor` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1153 |
| 1188 | `const.structured` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1154 |
| 1189 | `const.syntactic` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1155 |
| 1190 | `const.text` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1156 |
| 1191 | `const.timeseries` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1157 |
| 1192 | `const.timestamp` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1158 |
| 1193 | `const.video` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1159 |
| 1194 | `const.no` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1160 |
| 1195 | `const.yes` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1161 |
| 1196 | `const.ai_EnergyConsumption` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumption` | 1162 |
| 1197 | `const.ai_EnergyConsumptionDescription` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumptionDescription` | 1163 |
| 1198 | `const.kilowattHour` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1164 |
| 1199 | `const.megajoule` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1165 |
| 1200 | `const.ai_EnergyUnitType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType` | 1166 |
| 1201 | `const.spdx_AI_EnergyUnitType_kilowattHour` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1167 |
| 1202 | `const.spdx_AI_EnergyUnitType_megajoule` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1168 |
| 1203 | `const.spdx_AI_EnergyUnitType_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1169 |
| 1204 | `const.ai_SafetyRiskAssessmentType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType` | 1170 |
| 1205 | `const.spdx_AI_SafetyRiskAssessmentType_high` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1171 |
| 1206 | `const.spdx_AI_SafetyRiskAssessmentType_low` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1172 |
| 1207 | `const.spdx_AI_SafetyRiskAssessmentType_medium` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1173 |
| 1208 | `const.spdx_AI_SafetyRiskAssessmentType_serious` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1174 |
| 1209 | `const.ai_AIPackage` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/AI/AIPackage` | 1175 |
| 1210 | `const.serious` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1176 |
| 1211 | `const.build_Build` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Build/Build` | 1177 |
| 1212 | `const.extension_CdxPropertyEntry` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertyEntry` | 1178 |
| 1213 | `const.extension_CdxPropertiesExtension` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertiesExtension` | 1179 |
| 1214 | `const.AnnotationType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType` | 1180 |
| 1215 | `const.spdx_Core_AnnotationType_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1181 |
| 1216 | `const.spdx_Core_AnnotationType_review` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1182 |
| 1217 | `const.CreationInfo` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/CreationInfo` | 1183 |
| 1218 | `const.DictionaryEntry` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/DictionaryEntry` | 1184 |
| 1219 | `const.NoAssertionElement` | Special singleton term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/NoAssertionElement` | 1185 |
| 1220 | `const.NoneElement` | Special singleton term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/NoneElement` | 1186 |
| 1221 | `const.SpdxOrganization` | Special singleton term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/SpdxOrganization` | 1187 |
| 1222 | `const.ai` | Profile/namespace alias | CDDL-only or derived alias | `` | 1188 |
| 1223 | `const.core` | Profile/namespace alias | CDDL-only or derived alias | `` | 1189 |
| 1224 | `const.dataset` | Profile/namespace alias | CDDL-only or derived alias | `` | 1190 |
| 1225 | `const.expandedLicensing` | Profile/namespace alias | CDDL-only or derived alias | `` | 1191 |
| 1226 | `const.extension` | Profile/namespace alias | JSON-LD object term | `https://spdx.org/rdf/3.0.1/terms/Core/extension` | 1192 |
| 1227 | `const.lite` | Profile/namespace alias | CDDL-only or derived alias | `` | 1193 |
| 1228 | `const.security` | Profile/namespace alias | CDDL-only or derived alias | `` | 1194 |
| 1229 | `const.simpleLicensing` | Profile/namespace alias | CDDL-only or derived alias | `` | 1195 |
| 1230 | `const.software` | Profile/namespace alias | CDDL-only or derived alias | `` | 1196 |
| 1231 | `const.ExternalIdentifier` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifier` | 1197 |
| 1232 | `const.cpe22` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1198 |
| 1233 | `const.cpe23` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1199 |
| 1234 | `const.cve` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1200 |
| 1235 | `const.email` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1201 |
| 1236 | `const.packageUrl` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1202 |
| 1237 | `const.securityOther` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1203 |
| 1238 | `const.swid` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1204 |
| 1239 | `const.urlScheme` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1205 |
| 1240 | `const.ExternalIdentifierType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType` | 1206 |
| 1241 | `const.spdx_Core_ExternalIdentifierType_cpe22` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1207 |
| 1242 | `const.spdx_Core_ExternalIdentifierType_cpe23` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1208 |
| 1243 | `const.spdx_Core_ExternalIdentifierType_cve` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1209 |
| 1244 | `const.spdx_Core_ExternalIdentifierType_email` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1210 |
| 1245 | `const.spdx_Core_ExternalIdentifierType_gitoid` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1211 |
| 1246 | `const.spdx_Core_ExternalIdentifierType_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1212 |
| 1247 | `const.spdx_Core_ExternalIdentifierType_packageUrl` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1213 |
| 1248 | `const.spdx_Core_ExternalIdentifierType_securityOther` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1214 |
| 1249 | `const.spdx_Core_ExternalIdentifierType_swhid` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1215 |
| 1250 | `const.spdx_Core_ExternalIdentifierType_swid` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1216 |
| 1251 | `const.spdx_Core_ExternalIdentifierType_urlScheme` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1217 |
| 1252 | `const.ExternalMap` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/ExternalMap` | 1218 |
| 1253 | `const.ExternalRef` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/ExternalRef` | 1219 |
| 1254 | `const.altDownloadLocation` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1220 |
| 1255 | `const.altWebPage` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1221 |
| 1256 | `const.binaryArtifact` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1222 |
| 1257 | `const.bower` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1223 |
| 1258 | `const.buildMeta` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1224 |
| 1259 | `const.buildSystem` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1225 |
| 1260 | `const.certificationReport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1226 |
| 1261 | `const.chat` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1227 |
| 1262 | `const.componentAnalysisReport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1228 |
| 1263 | `const.cwe` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1229 |
| 1264 | `const.dynamicAnalysisReport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1230 |
| 1265 | `const.eolNotice` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1231 |
| 1266 | `const.exportControlAssessment` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1232 |
| 1267 | `const.funding` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1233 |
| 1268 | `const.issueTracker` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1234 |
| 1269 | `const.license` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1235 |
| 1270 | `const.mailingList` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1236 |
| 1271 | `const.mavenCentral` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1237 |
| 1272 | `const.metrics` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1238 |
| 1273 | `const.npm` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1239 |
| 1274 | `const.nuget` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1240 |
| 1275 | `const.privacyAssessment` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1241 |
| 1276 | `const.productMetadata` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1242 |
| 1277 | `const.purchaseOrder` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1243 |
| 1278 | `const.qualityAssessmentReport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1244 |
| 1279 | `const.releaseHistory` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1245 |
| 1280 | `const.releaseNotes` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1246 |
| 1281 | `const.riskAssessment` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1247 |
| 1282 | `const.runtimeAnalysisReport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1248 |
| 1283 | `const.secureSoftwareAttestation` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1249 |
| 1284 | `const.securityAdversaryModel` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1250 |
| 1285 | `const.securityAdvisory` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1251 |
| 1286 | `const.securityFix` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1252 |
| 1287 | `const.securityPenTestReport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1253 |
| 1288 | `const.securityPolicy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1254 |
| 1289 | `const.securityThreatModel` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1255 |
| 1290 | `const.socialMedia` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1256 |
| 1291 | `const.sourceArtifact` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1257 |
| 1292 | `const.staticAnalysisReport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1258 |
| 1293 | `const.support` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1259 |
| 1294 | `const.vcs` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1260 |
| 1295 | `const.vulnerabilityDisclosureReport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1261 |
| 1296 | `const.vulnerabilityExploitabilityAssessment` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1262 |
| 1297 | `const.ExternalRefType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType` | 1263 |
| 1298 | `const.spdx_Core_ExternalRefType_altDownloadLocation` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1264 |
| 1299 | `const.spdx_Core_ExternalRefType_altWebPage` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1265 |
| 1300 | `const.spdx_Core_ExternalRefType_binaryArtifact` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1266 |
| 1301 | `const.spdx_Core_ExternalRefType_bower` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1267 |
| 1302 | `const.spdx_Core_ExternalRefType_buildMeta` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1268 |
| 1303 | `const.spdx_Core_ExternalRefType_buildSystem` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1269 |
| 1304 | `const.spdx_Core_ExternalRefType_certificationReport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1270 |
| 1305 | `const.spdx_Core_ExternalRefType_chat` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1271 |
| 1306 | `const.spdx_Core_ExternalRefType_componentAnalysisReport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1272 |
| 1307 | `const.spdx_Core_ExternalRefType_cwe` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1273 |
| 1308 | `const.spdx_Core_ExternalRefType_documentation` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1274 |
| 1309 | `const.spdx_Core_ExternalRefType_dynamicAnalysisReport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1275 |
| 1310 | `const.spdx_Core_ExternalRefType_eolNotice` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1276 |
| 1311 | `const.spdx_Core_ExternalRefType_exportControlAssessment` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1277 |
| 1312 | `const.spdx_Core_ExternalRefType_funding` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1278 |
| 1313 | `const.spdx_Core_ExternalRefType_issueTracker` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1279 |
| 1314 | `const.spdx_Core_ExternalRefType_license` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1280 |
| 1315 | `const.spdx_Core_ExternalRefType_mailingList` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1281 |
| 1316 | `const.spdx_Core_ExternalRefType_mavenCentral` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1282 |
| 1317 | `const.spdx_Core_ExternalRefType_metrics` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1283 |
| 1318 | `const.spdx_Core_ExternalRefType_npm` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1284 |
| 1319 | `const.spdx_Core_ExternalRefType_nuget` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1285 |
| 1320 | `const.spdx_Core_ExternalRefType_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1286 |
| 1321 | `const.spdx_Core_ExternalRefType_privacyAssessment` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1287 |
| 1322 | `const.spdx_Core_ExternalRefType_productMetadata` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1288 |
| 1323 | `const.spdx_Core_ExternalRefType_purchaseOrder` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1289 |
| 1324 | `const.spdx_Core_ExternalRefType_qualityAssessmentReport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1290 |
| 1325 | `const.spdx_Core_ExternalRefType_releaseHistory` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1291 |
| 1326 | `const.spdx_Core_ExternalRefType_releaseNotes` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1292 |
| 1327 | `const.spdx_Core_ExternalRefType_riskAssessment` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1293 |
| 1328 | `const.spdx_Core_ExternalRefType_runtimeAnalysisReport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1294 |
| 1329 | `const.spdx_Core_ExternalRefType_secureSoftwareAttestation` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1295 |
| 1330 | `const.spdx_Core_ExternalRefType_securityAdversaryModel` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1296 |
| 1331 | `const.spdx_Core_ExternalRefType_securityAdvisory` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1297 |
| 1332 | `const.spdx_Core_ExternalRefType_securityFix` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1298 |
| 1333 | `const.spdx_Core_ExternalRefType_securityOther` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1299 |
| 1334 | `const.spdx_Core_ExternalRefType_securityPenTestReport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1300 |
| 1335 | `const.spdx_Core_ExternalRefType_securityPolicy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1301 |
| 1336 | `const.spdx_Core_ExternalRefType_securityThreatModel` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1302 |
| 1337 | `const.spdx_Core_ExternalRefType_socialMedia` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1303 |
| 1338 | `const.spdx_Core_ExternalRefType_sourceArtifact` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1304 |
| 1339 | `const.spdx_Core_ExternalRefType_staticAnalysisReport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1305 |
| 1340 | `const.spdx_Core_ExternalRefType_support` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1306 |
| 1341 | `const.spdx_Core_ExternalRefType_vcs` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1307 |
| 1342 | `const.spdx_Core_ExternalRefType_vulnerabilityDisclosureReport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1308 |
| 1343 | `const.spdx_Core_ExternalRefType_vulnerabilityExploitabilityAssessment` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1309 |
| 1344 | `const.HashAlgorithm` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm` | 1310 |
| 1345 | `const.spdx_Core_HashAlgorithm_adler32` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1311 |
| 1346 | `const.spdx_Core_HashAlgorithm_blake2b256` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1312 |
| 1347 | `const.spdx_Core_HashAlgorithm_blake2b384` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1313 |
| 1348 | `const.spdx_Core_HashAlgorithm_blake2b512` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1314 |
| 1349 | `const.spdx_Core_HashAlgorithm_blake3` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1315 |
| 1350 | `const.spdx_Core_HashAlgorithm_crystalsDilithium` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1316 |
| 1351 | `const.spdx_Core_HashAlgorithm_crystalsKyber` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1317 |
| 1352 | `const.spdx_Core_HashAlgorithm_falcon` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1318 |
| 1353 | `const.spdx_Core_HashAlgorithm_md2` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1319 |
| 1354 | `const.spdx_Core_HashAlgorithm_md4` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1320 |
| 1355 | `const.spdx_Core_HashAlgorithm_md5` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1321 |
| 1356 | `const.spdx_Core_HashAlgorithm_md6` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1322 |
| 1357 | `const.spdx_Core_HashAlgorithm_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1323 |
| 1358 | `const.spdx_Core_HashAlgorithm_sha1` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1324 |
| 1359 | `const.spdx_Core_HashAlgorithm_sha224` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1325 |
| 1360 | `const.spdx_Core_HashAlgorithm_sha256` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1326 |
| 1361 | `const.spdx_Core_HashAlgorithm_sha384` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1327 |
| 1362 | `const.spdx_Core_HashAlgorithm_sha3_224` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1328 |
| 1363 | `const.spdx_Core_HashAlgorithm_sha3_256` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1329 |
| 1364 | `const.spdx_Core_HashAlgorithm_sha3_384` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1330 |
| 1365 | `const.spdx_Core_HashAlgorithm_sha3_512` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1331 |
| 1366 | `const.spdx_Core_HashAlgorithm_sha512` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1332 |
| 1367 | `const.IndividualElement` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/IndividualElement` | 1333 |
| 1368 | `const.LifecycleScopeType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType` | 1334 |
| 1369 | `const.spdx_Core_LifecycleScopeType_build` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1335 |
| 1370 | `const.spdx_Core_LifecycleScopeType_design` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1336 |
| 1371 | `const.spdx_Core_LifecycleScopeType_development` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1337 |
| 1372 | `const.spdx_Core_LifecycleScopeType_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1338 |
| 1373 | `const.spdx_Core_LifecycleScopeType_runtime` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1339 |
| 1374 | `const.spdx_Core_LifecycleScopeType_test` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1340 |
| 1375 | `const.NamespaceMap` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/NamespaceMap` | 1341 |
| 1376 | `const.PackageVerificationCode` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/PackageVerificationCode` | 1342 |
| 1377 | `const.adler32` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1343 |
| 1378 | `const.blake2b256` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1344 |
| 1379 | `const.blake2b384` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1345 |
| 1380 | `const.blake2b512` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1346 |
| 1381 | `const.blake3` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1347 |
| 1382 | `const.crystalsDilithium` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1348 |
| 1383 | `const.crystalsKyber` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1349 |
| 1384 | `const.falcon` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1350 |
| 1385 | `const.md2` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1351 |
| 1386 | `const.md4` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1352 |
| 1387 | `const.md5` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1353 |
| 1388 | `const.md6` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1354 |
| 1389 | `const.sha1` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1355 |
| 1390 | `const.sha224` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1356 |
| 1391 | `const.sha256` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1357 |
| 1392 | `const.sha384` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1358 |
| 1393 | `const.sha3_224` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1359 |
| 1394 | `const.sha3_256` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1360 |
| 1395 | `const.sha3_384` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1361 |
| 1396 | `const.sha3_512` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1362 |
| 1397 | `const.sha512` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1363 |
| 1398 | `const.PositiveIntegerRange` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/PositiveIntegerRange` | 1364 |
| 1399 | `const.PresenceType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/PresenceType` | 1365 |
| 1400 | `const.spdx_Core_PresenceType_no` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1366 |
| 1401 | `const.spdx_Core_PresenceType_noAssertion` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1367 |
| 1402 | `const.spdx_Core_PresenceType_yes` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1368 |
| 1403 | `const.ProfileIdentifierType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType` | 1369 |
| 1404 | `const.spdx_Core_ProfileIdentifierType_ai` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1370 |
| 1405 | `const.spdx_Core_ProfileIdentifierType_build` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1371 |
| 1406 | `const.spdx_Core_ProfileIdentifierType_core` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1372 |
| 1407 | `const.spdx_Core_ProfileIdentifierType_dataset` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1373 |
| 1408 | `const.spdx_Core_ProfileIdentifierType_expandedLicensing` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1374 |
| 1409 | `const.spdx_Core_ProfileIdentifierType_extension` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1375 |
| 1410 | `const.spdx_Core_ProfileIdentifierType_lite` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1376 |
| 1411 | `const.spdx_Core_ProfileIdentifierType_security` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1377 |
| 1412 | `const.spdx_Core_ProfileIdentifierType_simpleLicensing` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1378 |
| 1413 | `const.spdx_Core_ProfileIdentifierType_software` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1379 |
| 1414 | `const.Relationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Relationship` | 1380 |
| 1415 | `const.complete` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1381 |
| 1416 | `const.incomplete` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1382 |
| 1417 | `const.affects` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1383 |
| 1418 | `const.amendedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1384 |
| 1419 | `const.ancestorOf` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1385 |
| 1420 | `const.availableFrom` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1386 |
| 1421 | `const.configures` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1387 |
| 1422 | `const.contains` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1388 |
| 1423 | `const.coordinatedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1389 |
| 1424 | `const.copiedTo` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1390 |
| 1425 | `const.delegatedTo` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1391 |
| 1426 | `const.dependsOn` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1392 |
| 1427 | `const.descendantOf` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1393 |
| 1428 | `const.describes` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1394 |
| 1429 | `const.doesNotAffect` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1395 |
| 1430 | `const.expandsTo` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1396 |
| 1431 | `const.exploitCreatedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1397 |
| 1432 | `const.fixedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1398 |
| 1433 | `const.fixedIn` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1399 |
| 1434 | `const.foundBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1400 |
| 1435 | `const.generates` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1401 |
| 1436 | `const.hasAddedFile` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1402 |
| 1437 | `const.hasAssessmentFor` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1403 |
| 1438 | `const.hasAssociatedVulnerability` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1404 |
| 1439 | `const.hasConcludedLicense` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1405 |
| 1440 | `const.hasDataFile` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1406 |
| 1441 | `const.hasDeclaredLicense` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1407 |
| 1442 | `const.hasDeletedFile` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1408 |
| 1443 | `const.hasDependencyManifest` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1409 |
| 1444 | `const.hasDistributionArtifact` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1410 |
| 1445 | `const.hasDocumentation` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1411 |
| 1446 | `const.hasDynamicLink` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1412 |
| 1447 | `const.hasEvidence` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1413 |
| 1448 | `const.hasExample` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1414 |
| 1449 | `const.hasHost` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1415 |
| 1450 | `const.hasInput` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1416 |
| 1451 | `const.hasMetadata` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1417 |
| 1452 | `const.hasOptionalComponent` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1418 |
| 1453 | `const.hasOptionalDependency` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1419 |
| 1454 | `const.hasOutput` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1420 |
| 1455 | `const.hasPrerequisite` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1421 |
| 1456 | `const.hasProvidedDependency` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1422 |
| 1457 | `const.hasRequirement` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1423 |
| 1458 | `const.hasSpecification` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1424 |
| 1459 | `const.hasStaticLink` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1425 |
| 1460 | `const.hasTest` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1426 |
| 1461 | `const.hasTestCase` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1427 |
| 1462 | `const.hasVariant` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1428 |
| 1463 | `const.invokedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1429 |
| 1464 | `const.modifiedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1430 |
| 1465 | `const.packagedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1431 |
| 1466 | `const.patchedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1432 |
| 1467 | `const.publishedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1433 |
| 1468 | `const.reportedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1434 |
| 1469 | `const.republishedBy` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1435 |
| 1470 | `const.serializedInArtifact` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1436 |
| 1471 | `const.testedOn` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1437 |
| 1472 | `const.trainedOn` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1438 |
| 1473 | `const.underInvestigationFor` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1439 |
| 1474 | `const.usesTool` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1440 |
| 1475 | `const.RelationshipCompleteness` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness` | 1441 |
| 1476 | `const.spdx_Core_RelationshipCompleteness_complete` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1442 |
| 1477 | `const.spdx_Core_RelationshipCompleteness_incomplete` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1443 |
| 1478 | `const.spdx_Core_RelationshipCompleteness_noAssertion` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1444 |
| 1479 | `const.RelationshipType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType` | 1445 |
| 1480 | `const.spdx_Core_RelationshipType_affects` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1446 |
| 1481 | `const.spdx_Core_RelationshipType_amendedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1447 |
| 1482 | `const.spdx_Core_RelationshipType_ancestorOf` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1448 |
| 1483 | `const.spdx_Core_RelationshipType_availableFrom` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1449 |
| 1484 | `const.spdx_Core_RelationshipType_configures` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1450 |
| 1485 | `const.spdx_Core_RelationshipType_contains` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1451 |
| 1486 | `const.spdx_Core_RelationshipType_coordinatedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1452 |
| 1487 | `const.spdx_Core_RelationshipType_copiedTo` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1453 |
| 1488 | `const.spdx_Core_RelationshipType_delegatedTo` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1454 |
| 1489 | `const.spdx_Core_RelationshipType_dependsOn` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1455 |
| 1490 | `const.spdx_Core_RelationshipType_descendantOf` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1456 |
| 1491 | `const.spdx_Core_RelationshipType_describes` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1457 |
| 1492 | `const.spdx_Core_RelationshipType_doesNotAffect` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1458 |
| 1493 | `const.spdx_Core_RelationshipType_expandsTo` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1459 |
| 1494 | `const.spdx_Core_RelationshipType_exploitCreatedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1460 |
| 1495 | `const.spdx_Core_RelationshipType_fixedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1461 |
| 1496 | `const.spdx_Core_RelationshipType_fixedIn` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1462 |
| 1497 | `const.spdx_Core_RelationshipType_foundBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1463 |
| 1498 | `const.spdx_Core_RelationshipType_generates` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1464 |
| 1499 | `const.spdx_Core_RelationshipType_hasAddedFile` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1465 |
| 1500 | `const.spdx_Core_RelationshipType_hasAssessmentFor` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1466 |
| 1501 | `const.spdx_Core_RelationshipType_hasAssociatedVulnerability` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1467 |
| 1502 | `const.spdx_Core_RelationshipType_hasConcludedLicense` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1468 |
| 1503 | `const.spdx_Core_RelationshipType_hasDataFile` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1469 |
| 1504 | `const.spdx_Core_RelationshipType_hasDeclaredLicense` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1470 |
| 1505 | `const.spdx_Core_RelationshipType_hasDeletedFile` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1471 |
| 1506 | `const.spdx_Core_RelationshipType_hasDependencyManifest` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1472 |
| 1507 | `const.spdx_Core_RelationshipType_hasDistributionArtifact` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1473 |
| 1508 | `const.spdx_Core_RelationshipType_hasDocumentation` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1474 |
| 1509 | `const.spdx_Core_RelationshipType_hasDynamicLink` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1475 |
| 1510 | `const.spdx_Core_RelationshipType_hasEvidence` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1476 |
| 1511 | `const.spdx_Core_RelationshipType_hasExample` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1477 |
| 1512 | `const.spdx_Core_RelationshipType_hasHost` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1478 |
| 1513 | `const.spdx_Core_RelationshipType_hasInput` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1479 |
| 1514 | `const.spdx_Core_RelationshipType_hasMetadata` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1480 |
| 1515 | `const.spdx_Core_RelationshipType_hasOptionalComponent` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1481 |
| 1516 | `const.spdx_Core_RelationshipType_hasOptionalDependency` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1482 |
| 1517 | `const.spdx_Core_RelationshipType_hasOutput` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1483 |
| 1518 | `const.spdx_Core_RelationshipType_hasPrerequisite` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1484 |
| 1519 | `const.spdx_Core_RelationshipType_hasProvidedDependency` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1485 |
| 1520 | `const.spdx_Core_RelationshipType_hasRequirement` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1486 |
| 1521 | `const.spdx_Core_RelationshipType_hasSpecification` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1487 |
| 1522 | `const.spdx_Core_RelationshipType_hasStaticLink` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1488 |
| 1523 | `const.spdx_Core_RelationshipType_hasTest` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1489 |
| 1524 | `const.spdx_Core_RelationshipType_hasTestCase` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1490 |
| 1525 | `const.spdx_Core_RelationshipType_hasVariant` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1491 |
| 1526 | `const.spdx_Core_RelationshipType_invokedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1492 |
| 1527 | `const.spdx_Core_RelationshipType_modifiedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1493 |
| 1528 | `const.spdx_Core_RelationshipType_other` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1494 |
| 1529 | `const.spdx_Core_RelationshipType_packagedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1495 |
| 1530 | `const.spdx_Core_RelationshipType_patchedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1496 |
| 1531 | `const.spdx_Core_RelationshipType_publishedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1497 |
| 1532 | `const.spdx_Core_RelationshipType_reportedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1498 |
| 1533 | `const.spdx_Core_RelationshipType_republishedBy` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1499 |
| 1534 | `const.spdx_Core_RelationshipType_serializedInArtifact` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1500 |
| 1535 | `const.spdx_Core_RelationshipType_testedOn` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1501 |
| 1536 | `const.spdx_Core_RelationshipType_trainedOn` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1502 |
| 1537 | `const.spdx_Core_RelationshipType_underInvestigationFor` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1503 |
| 1538 | `const.spdx_Core_RelationshipType_usesTool` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1504 |
| 1539 | `const.SpdxDocument` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/SpdxDocument` | 1505 |
| 1540 | `const.SupportType` | Vocabulary/type class | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/SupportType` | 1506 |
| 1541 | `const.spdx_Core_SupportType_deployed` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1507 |
| 1542 | `const.spdx_Core_SupportType_development` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1508 |
| 1543 | `const.spdx_Core_SupportType_endOfSupport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1509 |
| 1544 | `const.spdx_Core_SupportType_limitedSupport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1510 |
| 1545 | `const.spdx_Core_SupportType_noAssertion` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1511 |
| 1546 | `const.spdx_Core_SupportType_noSupport` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1512 |
| 1547 | `const.spdx_Core_SupportType_support` | Fully-qualified vocabulary member | CDDL-only or derived alias | `` | 1513 |
| 1548 | `const.Tool` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Tool` | 1514 |
| 1549 | `const.Agent` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Agent` | 1515 |
| 1550 | `const.Annotation` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Annotation` | 1516 |
| 1551 | `const.review` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1517 |
| 1552 | `const.development` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1518 |
| 1553 | `const.endOfSupport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1519 |
| 1554 | `const.limitedSupport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1520 |
| 1555 | `const.noSupport` | Local vocabulary member alias | CDDL-only or derived alias | `` | 1521 |
| 1556 | `const.Bundle` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Bundle` | 1522 |
| 1557 | `const.Hash` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Hash` | 1523 |
| 1558 | `const.LifecycleScopedRelationship` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopedRelationship` | 1524 |
| 1559 | `const.Organization` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Organization` | 1525 |
| 1560 | `const.Person` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Person` | 1526 |
| 1561 | `const.SoftwareAgent` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/SoftwareAgent` | 1527 |
| 1562 | `const.Bom` | Object/class term | JSON-LD string term | `https://spdx.org/rdf/3.0.1/terms/Core/Bom` | 1528 |
