#!/usr/bin/env python3
import libConfig, libPrint, pathlib
import libStringtie

Estimating = libStringtie.estimator()
Estimating.branchStr = "testing"
Estimating.directEstimating = True
Estimating.headerStr = "dsStringtie"
Estimating.estimating()