# FIXCAT Peer Review Agent - Usage Guide

## Quick Start

### Installation

1. Install dependencies:
```bash
cd agents/fixcat-peer-review
pip install -r requirements.txt
```

2. Verify installation:
```bash
python fixcat_agent.py --help
```

## Basic Usage

### Analyze a Single File

```bash
python fixcat_agent.py --input examples/sample_logrec.txt --output report.html
```

This will:
- Parse the FIXCAT/LOGREC file
- Analyze messages for issues
- Apply review rules
- Generate an HTML report

### Specify Output Format

```bash
# HTML report (default)
python fixcat_agent.py -i input.txt -o report.html -f html

# JSON report
python fixcat_agent.py -i input.txt -o report.json -f json

# Markdown report
python fixcat_agent.py -i input.txt -o report.md -f markdown
```

### Use Custom Configuration

```bash
python fixcat_agent.py -i input.txt -o report.html -c config/custom.yaml
```

### Batch Processing

Process multiple files in a directory:

```bash
python fixcat_agent.py --input-dir ./logs --output-dir ./reports --format html
```

## Python API Usage

### Basic Example

```python
from fixcat_agent import FIXCATReviewer

# Initialize reviewer
reviewer = FIXCATReviewer(config_path='config/default.yaml')

# Analyze a file
results = reviewer.analyze_file('path/to/logrec.txt')

# Generate report
reviewer.generate_report(results, 'report.html', format='html')
```

### Advanced Example

```python
from src.parsers import FIXCATParser
from src.analyzers import IssueAnalyzer
from src.rules import ReviewRulesEngine
from src.reporters import ReportGenerator

# Parse messages
parser = FIXCATParser()
messages = parser.parse_file('logrec.txt')

# Analyze issues
analyzer = IssueAnalyzer('config/default.yaml')
issues = analyzer.analyze(messages)

# Apply custom rules
rules_engine = ReviewRulesEngine()
rule_findings = rules_engine.execute_rules(messages)

# Generate report
reporter = ReportGenerator()
all_issues = issues + rule_findings
reporter.generate_report(
    issues=all_issues,
    messages=messages,
    output_path='report.html',
    format='html'
)
```

## Configuration

### Custom Configuration File

Create a custom YAML configuration file:

```yaml
# custom_config.yaml
analysis:
  severity_levels:
    critical:
      - "ABEND"
      - "SYSTEM FAILURE"
    high:
      - "ERROR"
      - "EXCEPTION"

rules:
  checks:
    - name: "Custom Check"
      description: "My custom check"
      threshold: 5
      timeframe: "2h"
      severity: "high"

ptf_mapping:
  S0C4:
    - "Custom recommendation 1"
    - "Custom recommendation 2"
```

Use it:
```bash
python fixcat_agent.py -i input.txt -o report.html -c custom_config.yaml
```

## Understanding the Output

### HTML Report Sections

1. **Executive Summary**: High-level overview of findings
2. **Severity Breakdown**: Issues categorized by severity
3. **Issues List**: Detailed list of all identified issues
4. **Recommendations**: Actionable recommendations for each issue

### JSON Report Structure

```json
{
  "metadata": {
    "input_file": "logrec.txt",
    "statistics": {...}
  },
  "summary": {
    "total_issues": 10,
    "critical_issues": 2,
    "high_issues": 5
  },
  "issues": [
    {
      "issue_id": "ABEND-S0C4",
      "title": "Frequent ABEND S0C4",
      "severity": "HIGH",
      "category": "ABEND",
      "occurrences": 4,
      "recommendations": [...]
    }
  ]
}
```

## Common Use Cases

### 1. Daily System Health Check

```bash
# Run daily analysis
python fixcat_agent.py \
  --input /var/log/mainframe/logrec.txt \
  --output /reports/daily_$(date +%Y%m%d).html \
  --format html
```

### 2. Pre-Production Review

```bash
# Analyze test environment logs
python fixcat_agent.py \
  --input-dir /logs/test_env \
  --output-dir /reports/pre_prod \
  --format json
```

### 3. Incident Investigation

```bash
# Generate detailed markdown report
python fixcat_agent.py \
  --input incident_logs.txt \
  --output incident_analysis.md \
  --format markdown
```

### 4. Compliance Audit

```bash
# Generate JSON for automated processing
python fixcat_agent.py \
  --input audit_logs.txt \
  --output audit_report.json \
  --format json
```

## Interpreting Results

### Severity Levels

- **CRITICAL**: Immediate attention required (security violations, system failures)
- **HIGH**: Significant issues requiring prompt action (frequent ABENDs, storage issues)
- **MEDIUM**: Issues that should be addressed (performance degradation, recurring errors)
- **LOW**: Informational findings (warnings, notices)

### Common Issue Categories

- **ABEND**: Application or system ABENDs
- **STORAGE**: Storage management issues (B37, D37, E37)
- **SECURITY**: RACF violations and unauthorized access
- **PERFORMANCE**: Timeouts and performance degradation
- **DATA**: Data integrity issues (S0C7, data exceptions)
- **PATTERN**: Recurring error patterns
- **JOB**: Job failure patterns
- **RESOURCE**: Resource contention issues

## Troubleshooting

### Parse Errors

If you see parse errors:
```
Warning: 5 parse errors occurred
```

Check:
- File encoding (should be UTF-8 or ASCII)
- Message format consistency
- Timestamp formats

### No Issues Found

If no issues are detected:
- Verify input file contains error messages
- Check configuration thresholds
- Review severity mappings

### Performance Issues

For large files:
- Use batch processing with smaller chunks
- Adjust `max_file_size_mb` in config
- Enable parallel processing

## Best Practices

1. **Regular Reviews**: Run daily or after significant changes
2. **Baseline Establishment**: Create baseline reports for comparison
3. **Custom Rules**: Add organization-specific rules
4. **Trend Analysis**: Compare reports over time
5. **Integration**: Integrate with CI/CD pipelines
6. **Documentation**: Document custom configurations

## Integration Examples

### Jenkins Pipeline

```groovy
stage('FIXCAT Review') {
    steps {
        sh '''
            python fixcat_agent.py \
              --input ${WORKSPACE}/logs/logrec.txt \
              --output ${WORKSPACE}/reports/fixcat_report.html
        '''
        publishHTML([
            reportDir: 'reports',
            reportFiles: 'fixcat_report.html',
            reportName: 'FIXCAT Review'
        ])
    }
}
```

### Cron Job

```bash
# Daily at 2 AM
0 2 * * * /usr/bin/python3 /opt/fixcat/fixcat_agent.py \
  --input /var/log/logrec.txt \
  --output /reports/daily_$(date +\%Y\%m\%d).html
```

## Support

For issues or questions:
- Check the README.md for detailed documentation
- Review example configurations in config/
- Examine sample data in examples/