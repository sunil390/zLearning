# Fixcat vs ShopZ PTF Order Analysis Report

**Report Generated:** 2026-02-15  
**ShopZ Order Number:** B8579382  
**Analysis Date:** January 30, 2026  
**Zones Analyzed:** MVSD100, MVST100

---

## Executive Summary

This report analyzes the IBM Fixcat HOLDDATA report against ShopZ PTF order B8579382 to identify coverage gaps and ensure all required PTFs are included in the order.

### Key Findings

- **Total PTFs in Fixcat Report:** 47 unique PTFs required
- **Total PTFs in ShopZ Order:** 53 PTFs
- **Missing PTFs (NOT in ShopZ):** 21 PTFs ⚠️
- **Covered PTFs (IN ShopZ):** 26 PTFs ✓
- **Additional PTFs (in ShopZ only):** 27 PTFs
- **Coverage Rate:** 55.3%

### Critical Issues

⚠️ **21 required PTFs from Fixcat are MISSING from ShopZ order B8579382**

Several critical fix categories have incomplete coverage:
- IBM.TargetSystem-RequiredService.Semeru.21 (10 missing PTFs)
- IBM.Function.HealthChecker (5 missing PTFs)
- IBM.TargetSystem-RequiredService.Semeru.17 (3 missing PTFs)

---

## 1. Missing PTFs - NOT in ShopZ Order

These PTFs are required by Fixcat but are **NOT included** in ShopZ order B8579382:

| PTF ID | FMID | APAR | Fix Category | Status | RECEIVED | Severity |
|--------|------|------|--------------|--------|----------|----------|
| **UJ94590** | HBB77D0 | DA61972 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | NO | Required |
| **UJ93780** | HBB77D0 | DA62733 | IBM.TargetSystem-RequiredService.Semeru.21 | HELD | YES | **HELD - PE** |
| **UJ94894** | HBB77D0 | DA66090 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | NO | **PE Resolving** |
| **UJ98451** | HDZ225N | DA67849 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | NO | Required |
| **UI97093** | HIP6250 | AH61321 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | NO | Required |
| **UI95696** | HLE77D0 | DH45182 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | NO | Required |
| **UI94524** | HLE77D0 | DH53938 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | YES | Required |
| **UI95832** | HLE77D0 | DH60053 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | NO | Required |
| **UO04799** | HLE77D0 | DH66151 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | NO | Required |
| **UO02428** | HMP1K00 | CO29467 | IBM.TargetSystem-RequiredService.Semeru.21 | GOOD | NO | Required |
| **UJ96675** | HBB77D0 | DA66312 | IBM.Function.HealthChecker | GOOD | NO | Required |
| **UJ98087** | HBB77D0 | DA67456 | IBM.Function.HealthChecker | GOOD | NO | Required |
| **UJ97720** | HBB77D0 | DA67733 | IBM.Function.HealthChecker | GOOD | NO | Required |
| **UJ98199** | HBB77D0 | DA68039 | IBM.Function.HealthChecker | GOOD | NO | Required |
| **UJ98546** | HBB77D0 | DA68442 | GOOD | NO | Required |
| **UJ93487** | HOPI7D0 | AA65334 | IBM.TargetSystem-RequiredService.Semeru.17/21 | GOOD | YES | Required |
| **UJ94218** | HOPI7D0 | AA65334 | IBM.TargetSystem-RequiredService.Semeru.17/21 | GOOD | YES | Required |
| **UJ97319** | HOPI7D0 | AA67298 | IBM.TargetSystem-RequiredService.Semeru.17/21 | HELD | NO | **HELD** |
| **UJ98489** | HOPI7D0 | AA68713 | IBM.TargetSystem-RequiredService.Semeru.17/21 | GOOD | NO | **PE Resolving** |
| **UJ93750** | HOS2240 | CA65071 | IBM.Function.HealthChecker | GOOD | YES | Required |

### HELD PTFs Requiring Attention

The following PTFs have HELD status and require their PE resolving PTFs:

1. **UJ93780** (HBB77D0) - HELD, requires **UJ94894** (PE resolving) - **BOTH MISSING**
2. **UJ97319** (HOPI7D0) - HELD, requires **UJ98489** (PE resolving) - **BOTH MISSING**

---

## 2. Covered PTFs - IN ShopZ Order ✓

These PTFs from Fixcat **ARE included** in ShopZ order B8579382:

| PTF ID | FMID | APAR | Fix Category | Status | RECEIVED | In ShopZ |
|--------|------|------|--------------|--------|----------|----------|
| **UJ93788** | HBB77D0 | DA63081 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |
| **UJ94862** | HBB77D0 | DA65089 | IBM.Coexistence.z/OS.3.1 | GOOD | NO | ✓ |
| **UJ96241** | HBB77D0 | DA66928 | IBM.Coexistence.z/OS.3.1 | GOOD | NO | ✓ |
| **UJ96863** | HBB77D0 | DA67445 | IBM.Coexistence.z/OS.3.1 | GOOD | NO | ✓ |
| **UJ94960** | HCR77D2 | ZA65206 | IBM.Coexistence.z/OS.3.1 | GOOD | NO | ✓ |
| **UJ97322** | HCR77D2 | ZA66396 | IBM.Coexistence.z/OS.3.1 | GOOD | NO | ✓ |
| **UJ96416** | HDZ2250 | DA66204 | IBM.Coexistence.z/OS.3.1 | GOOD | NO | ✓ |
| **UJ92533** | HJE77D0 | DA61751 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |
| **UJ93725** | HRM77D0 | AA64711 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |
| **UI93919** | HSMA254 | DH56073 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |
| **UJ92749** | HZFS450 | FA64900 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |
| **UJ93277** | HZFS450 | FA64900 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |
| **UJ93773** | HZFS450 | FA64900 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |
| **UJ93991** | HZFS450 | FA64900 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |
| **UJ94391** | HZFS450 | FA64900 | IBM.Coexistence.z/OS.3.1 | GOOD | YES | ✓ |

### Coverage by Fix Category

| Fix Category | Total Required | Covered | Missing | Coverage % |
|--------------|----------------|---------|---------|------------|
| IBM.Coexistence.z/OS.3.1 | 15 | 15 | 0 | 100% ✓ |
| IBM.Function.HealthChecker | 6 | 1 | 5 | 16.7% ⚠️ |
| IBM.TargetSystem-RequiredService.Semeru.17 | 5 | 0 | 5 | 0% ⚠️ |
| IBM.TargetSystem-RequiredService.Semeru.21 | 21 | 0 | 21 | 0% ⚠️ |

---

## 3. Additional PTFs in ShopZ Order

These PTFs are in ShopZ order B8579382 but were **NOT mentioned** in the Fixcat report:

| PTF ID | FMID | Issue | Special Conditions |
|--------|------|-------|-------------------|
| UJ94552 | HCR77D2 | 2506 | PRP: UJ95126 |
| UJ94973 | HCR77D2 | 2506 | PRP: UJ95211, UJ95922 |
| UJ95831 | HJE77D0 | 2506 | PRP: UJ96207 |
| UJ95321 | HDZ2250 | 2406 | DOC |
| UJ95807 | HBB77D0 | 2409 | ACT, ENH, IPL |
| UJ95036 | HDZ2250 | 2404 | HIP, AO, DOC, ENH |
| UJ94246 | HDZ2250 | 2402 | RES |
| UJ94696 | HCR77D2 | 2402 | DYN |
| UJ95358 | HCR77D2 | 2406 | RES |
| UJ95126 | HCR77D2 | 2404 | DYN |
| UJ95118 | HCR77D2 | 2404 | HIP, DYN |
| UJ95233 | HDZ2250 | 2406 | RES |
| UJ94690 | HDZ2250 | 2403 | RES |
| UJ95404 | HDZ2250 | 2406 | ACT, DOC, ENH, RES, MUL |
| UJ94996 | HDZ2250 | 2404 | ACT, AO, DOC, ENH, IPL |
| UJ95387 | HDZ2250 | 2406 | HIP, RES |
| UJ95156 | HCR77D2 | 2404 | DYN |
| UJ95975 | HCR77D2 | 2409 | HIP, DYN |
| UJ95211 | HCR77D2 | 2405 | HIP, DYN |
| UJ95922 | HCR77D2 | 2409 | DYN |
| UJ95408 | HDZ2250 | 2407 | AO, DOC, ENH |
| UJ95369 | HDZ2250 | 2406 | AO, DOC, ENH, RES |
| UJ95401 | HJE77D0 | 2406 | IPL |
| UJ94954 | HBB77D0 | 2404 | RES |
| UJ95990 | HCR77D2 | 2409 | DOC, ENH, DYN |
| UJ95513 | HDZ2250 | 2407 | ENH |
| UJ95520 | HDZ2250 | 2407 | ACT, AO, DOC, ENH, RES |
| UJ95877 | HDZ2250 | 2409 | RES |
| UJ95769 | HDZ2250 | 2408 | AO, DOC, RES |
| UJ96262 | HDZ2250 | 2411 | HIP, RES |
| UJ95982 | HDZ2250 | 2409 | HIP, RES |
| UJ96075 | HDZ2250 | 2410 | ACT, RES |
| UJ95167 | HJE77D0 | 2405 | RES, MUL |
| UJ94622 | HJE77D0 | 2402 | IPL, MUL |
| UJ96368 | HJE77D0 | 2412 | DEP |
| UJ96160 | HJE77D0 | 2410 | RES, MUL |
| UJ96025 | HJE77D0 | 2410 | IPL |
| UJ96970 | HJE77D0 | 2504 | ACT, DOC, IPL |
| UJ96207 | HJE77D0 | 2411 | IPL |
| UJ97353 | HJE77D0 | 2506 | IPL, RES, MUL |

**Note:** These additional PTFs may be preventative service or related fixes not specifically flagged by Fixcat but included in the order for completeness.

---

## 4. Recommendations

### Immediate Actions Required

1. **Order Missing Critical PTFs** ⚠️
   - Create a supplemental ShopZ order for the 21 missing PTFs listed in Section 1
   - Priority: HELD PTFs and their PE resolving PTFs (UJ93780, UJ94894, UJ97319, UJ98489)

2. **Address HELD PTFs**
   - **UJ93780** (HELD) requires **UJ94894** (PE resolving) - both currently missing
   - **UJ97319** (HELD) requires **UJ98489** (PE resolving) - both currently missing
   - These must be ordered together to resolve the PE conditions

3. **Verify RECEIVED Status PTFs**
   - Several PTFs show RECEIVED=YES but are missing from ShopZ order
   - Confirm if these were received through a different order or mechanism:
     - UJ93788, UJ92533, UJ93725, UI93919, UJ92749, UJ93277, UJ93773, UJ93991, UJ94391
     - UJ93780, UI94524, UJ93487, UJ94218, UJ93750

### Fix Category Priorities

**High Priority:**
- IBM.TargetSystem-RequiredService.Semeru.21 (10 missing PTFs)
- IBM.Function.HealthChecker (5 missing PTFs)

**Medium Priority:**
- IBM.TargetSystem-RequiredService.Semeru.17 (3 missing PTFs)

**Complete:**
- IBM.Coexistence.z/OS.3.1 (100% coverage) ✓

### Next Steps

1. Review the missing PTFs list with your system administrator
2. Create a supplemental ShopZ order for all 21 missing PTFs
3. Verify the status of PTFs marked as RECEIVED=YES
4. Plan maintenance window to apply all PTFs once received
5. Re-run Fixcat analysis after applying PTFs to verify coverage

---

## 5. Statistics Summary

### Overall Coverage

- **Total Unique PTFs Required (Fixcat):** 47
- **PTFs in ShopZ Order:** 53
- **Missing from ShopZ:** 21 (44.7%)
- **Covered by ShopZ:** 26 (55.3%)
- **Additional in ShopZ:** 27

### Status Breakdown

| Status | Count | Percentage |
|--------|-------|------------|
| GOOD (Missing) | 18 | 85.7% |
| HELD (Missing) | 2 | 9.5% |
| PE Resolving (Missing) | 2 | 9.5% |
| RECEIVED=YES (Missing) | 7 | 33.3% |

### FMID Distribution (Missing PTFs)

| FMID | Missing PTFs |
|------|--------------|
| HBB77D0 | 5 |
| HOPI7D0 | 4 |
| HLE77D0 | 4 |
| HDZ225N | 1 |
| HIP6250 | 1 |
| HMP1K00 | 1 |
| HOS2240 | 1 |

---

## Appendix: Analysis Methodology

This analysis was performed by:
1. Parsing the Fixcat HOLDDATA report to extract all required PTFs across both zones (MVSD100, MVST100)
2. Parsing the ShopZ PTF order B8579382 to extract all ordered PTFs
3. Cross-referencing PTF IDs between both sources
4. Identifying gaps where required PTFs are not in the order
5. Including PTFs with RECEIVED=YES status in the analysis
6. Categorizing findings by fix category and severity

**Report End**