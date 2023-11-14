import os, sys
import bandit
from bandit.core import manager

#Local Class
from .utils import SharedUtils



class VulnerabilityScanner:
    def bandit_scan_report(self, base_path):
        b_mgr = manager.BanditManager(bandit.config.BanditConfig(), '')
        b_mgr.targets= [base_path]
        b_mgr.discover_files(b_mgr.targets, recursive=True)
        b_mgr.run_tests()
        results= b_mgr.get_issue_list()
        all_report= []
        for index, issue in enumerate(results):            
            issue_dict= issue.as_dict()
            all_report.append(issue_dict)
        return all_report