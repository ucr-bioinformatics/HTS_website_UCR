'use strict';

{
 pages: [
  {
   elements: [
    {
     type: "text",
     isRequired: true,
     name: "title",
     title: "Project Title"
    },
    {
     type: "text",
     isRequired: true,
     name: "name",
     title: "Name"
    },
    {
     type: "text",
     inputType: "email",
     isRequired: true,
     name: "email",
     title: "Email"
    },
    {
     type: "text",
     inputType: "tel",
     isRequired: true,
     name: "phoneNumber",
     title: "Telephone Number"
    },
    {
     type: "text",
     isRequired: true,
     name: "principleInvestigator",
     title: "Principal Investigator"
    },
    {
     type: "text",
     isRequired: true,
     name: "billingAccount",
     title: "Billing Account Number"
    },
    {
     type: "paneldynamic",
     name: "samples",
     title: "Samples",
     isRequired: true,
     templateElements: [
      {
       type: "text",
       isRequired: true,
       name: "label",
       startWithNewLine: false,
       title: "Label"
      },
      {
       type: "text",
       isRequired: true,
       name: "projectDescription",
       startWithNewLine: false,
       title: "Project Description"
      },
      {
       type: "text",
       isRequired: true,
       name: "organism",
       title: "Organism(s) (full scientific name)"
      },
      {
       type: "dropdown",
       choices: [
        "HiSeq 2500",
        "HiSeqRapidRun",
        "MiSeq",
        "NextSeq",
        "PacBio"
       ],
       isRequired: true,
       name: "sequencer",
       title: "Sequencer"
      },
      {
       type: "text",
       isRequired: true,
       name: "sampleType",
       placeHolder: "RNASeq, DNASeq, small RNA, etc",
       title: "Sample Type"
      },
      {
       type: "text",
       inputType: "number",
       isRequired: true,
       name: "dnaConcentration",
       title: "DNA Concentration (ng/ul)"
      },
      {
       type: "text",
       name: "smrtCells",
       title: "Number of SMRT Cells (PacBio only)",
       visible: false
      },
      {
       type: "dropdown",
       choices: [
        "30",
        "45",
        "55",
        "60",
        "75",
        "90",
        "105",
        "120",
        "135",
        "150",
        "165",
        "180",
        "195",
        "210",
        "225",
        "240",
        "255",
        "270",
        "285",
        "300",
        "315",
        "330",
        "345",
        "360"
       ],
       name: "movieLength",
       startWithNewLine: false,
       title: "Movie Length (in minutes) (PacBio only)"
      }
     ],
     panelCount: 1
    }
   ],
   name: "sequencer",
   title: "Sequencer"
  }
 ]
}