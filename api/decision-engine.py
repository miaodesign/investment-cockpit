"""
Decision Engine API Endpoint
"""
from datetime import datetime
import json

DECISION_DATA = {
    "success": True,
    "data": {
        "updateTime": datetime.now().strftime('%H:%M'),
        "market_env": {
            "level": "震荡偏多", "score": 65, "position_limit": 80,
            "dimensions": {
                "trend": {"score": 70, "status": "上升趋势"},
                "money": {"score": 60, "status": "资金流入"},
                "emotion": {"score": 65, "status": "情绪中性"}
            }
        },
        "signal": "谨慎乐观",
        "suggestions": [
            {"priority": "高", "action": "加仓腾讯", "reason": "港股反弹，技术面突破"},
            {"priority": "中", "action": "减仓平安", "reason": "保险板块承压"},
            {"priority": "中", "action": "持有茅台", "reason": "白酒旺季临近"},
            {"priority": "低", "action": "关注宁德", "reason": "新能源政策利好"}
        ],
        "position_rules": {"current": 90.2, "target": 85, "max": 80, "min": 60},
        "cross_risk": {"risk_level": "中等", "exposure": {"stock": 85, "bond": 10, "cash": 5}}
    }
}

def handler(environ, start_response):
    headers = [
        ('Content-Type', 'application/json; charset=utf-8'),
        ('Access-Control-Allow-Origin', '*'),
    ]
    body = json.dumps(DECISION_DATA)
    start_response('200', headers)
    return [body.encode('utf-8')]
