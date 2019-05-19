#!/usr/bin/env python3
import libConfig
# ---- Configuration of Experiment Design ---- 
expRep = libConfig.config()
expRep.queryStr = "testing"
expRep.folderStr = "config/"
# Arguments/Parameters below need to modify depend on 
# your experiment design and naming style
expRep.queryDict = {
    "branch" : "testing",
    "group" : ["Control","T1","T2","T3","T4","T5"],
    "replication" : ["r1"],
    "pairPostfix" : "pair",
    "unpairPostfix" : "unpair",
    "[dsStringtie]hisat2Condition" : "hisat2ForStringtie",
    "[dsStringtie]conditionList" : [("speciesTestingA","trimQ20"),("speciesTestingB","trimQ20"),("speciesTestingC","trimQ20")],
    "[dsStringtie]inputFileName" : "large/04-hisat2/testing/{annotateCondition}-{trimCondition}/{hisat2Condition}-{group}{replication}-sorted.bam",
    # above: large/04-hisat2/testing/speciesTestingA-trimQ20/hisat2ForStringtie-T1r1-sorted.bam
    "[dsStringtie]tsvFileName" : "data/05-ds-Stringtie/testing/{annotateCondition}-{trimCondition}/{group}{replication}-expression.tsv",
    # above: data/05-Stringtie/testing/speciesTestingA-trimQ20/T1r1-expression.tsv
    "[dsStringtie]ballgownFolder" : "data/05-ds-ballgown/testing/{annotateCondition}-{trimCondition}-{group}{replication}/",
    # above: data/06-ballgown/testing/speciesTestingA-trimQ20-T1r1/
    "[dsStringtie]gtfFileName" : "data/05-ds-ballgown/testing/{annotateCondition}-{trimCondition}-{group}{replication}/{group}{replication}-expression.gtf",
    # above: data/06-ballgown/testing/speciesTestingA-trimQ20-T1r1/T1r1-expression.gtf
    "testing" : False,
}
expRep.modeStr = "UPDATE"
expRep.save()

# ---- Configuration of Mapping Conditions ---- 
SpeA = libConfig.config()
SpeA.queryStr = "speciesTestingA"
SpeA.folderStr = "config/"
SpeA.queryDict = {
    "from" : "binHISAT2-BUILD",
    "seqPath" : "data/GenomeSequence/SpeA.fa",
    "antPath" : "data/GenomeSequence/SpeA.gff3",
    "indexHeader" : "data/02-hisat2Index/SpeA",
    "checkFolder"    : "data/02-hisat2Index/",
    "thread" : "6",
    "testing" : True,
}
SpeA.modeStr = "OVERWRITE"
SpeA.save()

SpeB = libConfig.config()
SpeB.queryStr = "speciesTestingB"
SpeB.folderStr = "config/"
SpeB.queryDict = {
    "from" : "binHISAT2-BUILD",
    "seqPath" : "data/GenomeSequence/SpeB.fna",
    "antPath" : "data/GenomeSequence/SpeB.gff3",
    "indexHeader" : "data/02-hisat2Index/SpeB",
    "checkFolder"    : "data/02-hisat2Index/",
    "thread" : "6",
    "testing" : True,
}
SpeB.modeStr = "OVERWRITE"
SpeB.save()

SpeC = libConfig.config()
SpeC.queryStr = "speciesTestingC"
SpeC.folderStr = "config/"
SpeC.queryDict = {
    "from" : "binHISAT2-BUILD",
    "seqPath" : "data/GenomeSequence/SpeC.fasta",
    "antPath" : "data/GenomeSequence/SpeC.gff3",
    "indexHeader" : "data/02-hisat2Index/SpeC",
    "checkFolder"    : "data/02-hisat2Index/",
    "thread" : "6",
    "testing" : True,
}
SpeC.modeStr = "OVERWRITE"
SpeC.save()

# ---- Configuration of Mapping Command ---- 
"""
Original command:
    stringtie [BAM file] -o [Result GTF file]\
        -p [Thread] -G [Reference GFF file] -e
"""

Stringtie = libConfig.config()
Stringtie.queryStr = "binStringTie-RUN"
Stringtie.folderStr = "config/"
Stringtie.queryDict = {
    "command" : 
        "bin/stringtie/stringtie {bamfile} -v -o {outputfile} "+
        "-p {thread} -G {antPath}"
}
Stringtie.modeStr = "UPDATE"
Stringtie.save()

Stringtie = libConfig.config()
Stringtie.queryStr = "binStringTie-RUN-withoutAnnotation"
Stringtie.folderStr = "config/"
Stringtie.queryDict = {
    "command" : 
        "bin/stringtie/stringtie {bamfile} -v -o {outputfile} "+
        "-p {thread}"
}
Stringtie.modeStr = "UPDATE"
Stringtie.save()

StMerge = libConfig.config()
StMerge.queryStr = "binStringTie-MERGE"
StMerge.folderStr = "config/"
StMerge.queryDict = {
    "command" : 
        "bin/stringtie/stringtie {inputfiles} --merge -v -o {outputfile} "+
        "-p {thread}"
}
StMerge.modeStr = "UPDATE"
StMerge.save()

StEstimate = libConfig.config()
StEstimate.queryStr = "binStringTie-ESTIMATE"
StEstimate.folderStr = "config/"
StEstimate.queryDict = {
    "command" : 
        "bin/stringtie/stringtie {bamfile} -v "+
        "-b {ballgownPath} " +
        "-p {thread} -G {mergePath} " +
        "-o {gtffile} "        
        "-e -A {tsvfile}"        
}
StEstimate.modeStr = "UPDATE"
StEstimate.save()