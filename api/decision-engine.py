from datetime import datetime
import json

def handler(environ, start_response):
    data = {
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
            "kpi": {
                "win_rate": {"value": 68.5, "label": "胜率", "color": "green", "type": "percent"},
                "profit_factor": {"value": 2.35, "label": "盈亏比", "color": "green", "type": "number"},
                "max_drawdown": {"value": -12.8, "label": "最大回撤", "color": "red", "type": "percent"},
                "sharpe": {"value": 1.85, "label": "夏普比率", "color": "green", "type": "number"}
            },
            "position_rules": {"current": 90.2, "target": 85, "max": 80, "min": 60},
            "cross_risk": {"risk_level": "中等", "exposure": {"股票": 85, "债券": 10, "现金": 5}}
        }
    }
    body = json.dumps(data)
    start_response('200', [('Content-Type', 'application/json; charset=utf-8'), ('Access-Control-Allow-Origin', '*')])
    return [body.encode('utf-8')]
