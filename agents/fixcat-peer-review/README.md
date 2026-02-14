# Mainframe FIXCAT Peer Review Agent

## Overview
An intelligent peer review agent for mainframe FIXCAT (Fix Category) analysis. This agent automates the review of IBM mainframe system error messages, LOGREC data, and system diagnostics to identify issues, suggest fixes, and provide actionable insights.

## What is FIXCAT?
FIXCAT (Fix Category) is IBM's classification system for mainframe fixes and PTFs (Program Temporary Fixes). It helps categorize system errors, ABEND codes, and diagnostic messages to facilitate problem determination and resolution.

## Features
- **Automated FIXCAT Analysis**: Parse and analyze FIXCAT messages from LOGREC, SYSLOG, and other sources
- **Pattern Recognition**: Identify recurring issues and error patterns
- **Severity Assessment**: Classify issues by severity (Critical, High, Medium, Low)
- **Fix Recommendations**: Suggest applicable PTFs and fixes based on error patterns
- **Compliance Checking**: Verify system configurations against IBM best practices
- **Report Generation**: Create detailed peer review reports in multiple formats

## Architecture
```
fixcat-peer-review/
├── src/
│   ├── parsers/          # FIXCAT message parsers
│   ├── analyzers/        # Analysis engines
│   ├── rules/            # Review rules and patterns
│   └── reporters/        # Report generators
├── config/               # Configuration files
├── tests/                # Test cases
└── examples/             # Sample FIXCAT data
```

## Usage

### Basic Usage
```python
from fixcat_agent import FIXCATReviewer

# Initialize the reviewer
reviewer = FIXCATReviewer(config_path='config/default.yaml')

# Analyze FIXCAT data
results = reviewer.analyze_file('path/to/logrec.txt')

# Generate report
reviewer.generate_report(results, output='review_report.html')
```

### Command Line
```bash
# Analyze a single file
python fixcat_agent.py --input logrec.txt --output report.html

# Analyze multiple files
python fixcat_agent.py --input-dir ./logs --output-dir ./reports

# Use custom rules
python fixcat_agent.py --input logrec.txt --rules custom_rules.yaml
```

## Configuration
See [`config/default.yaml`](config/default.yaml) for configuration options.

## Requirements
- Python 3.8+
- PyYAML
- Jinja2 (for report generation)
- pandas (for data analysis)

## Installation
```bash
pip install -r requirements.txt
```

## Contributing
Contributions welcome! Please read the contributing guidelines before submitting PRs.

## License
MIT License