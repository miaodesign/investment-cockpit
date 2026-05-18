"""
Vercel Serverless API - 投资驾驶舱
"""
from datetime import datetime
import json

# 持仓数据
PORTFOLIO_DATA = {
    "success": True,
    "data": {
        "accounts": [
            {
                "key": "guolian",
                "label": "国联",
                "stocks": [
                    {"Name": "腾讯控股", "code": "00700.HK", "qty": 100, "cost": 380.5, "price": 385.2, "pnl": 470, "pnlPct": 1.24},
                    {"Name": "阿里巴巴", "code": "09988.HK", "qty": 200, "cost": 85.3, "price": 82.1, "pnl": -640, "pnlPct": -3.75},
                    {"Name": "美团", "code": "03690.HK", "qty": 150, "cost": 120.8, "price": 125.5, "pnl": 705, "pnlPct": 3.89}
                ]
            },
            {
                "key": "guoxin",
                "label": "国信",
                "stocks": [
                    {"Name": "贵州茅台", "code": "600519.SH", "qty": 50, "cost": 1680.0, "price": 1725.5, "pnl": 2275, "pnlPct": 2.71},
                    {"Name": "宁德时代", "code": "300750.SZ", "qty": 80, "cost": 210.5, "price": 208.3, "pnl": -176, "pnlPct": -1.05}
                ]
            },
            {
                "key": "guangfa",
                "label": "广发",
                "stocks": [
                    {"Name": "比亚迪", "code": "002594.SZ", "qty": 120, "cost": 245.8, "price": 258.6, "pnl": 1536, "pnlPct": 5.21},
                    {"Name": "五粮液", "code": "000858.SZ", "qty": 100, "cost": 158.2, "price": 152.8, "pnl": -540, "pnlPct": -3.41}
                ]
            },
            {
                "key": "huatai",
                "label": "华泰",
                "stocks": [
                    {"Name": "中国平安", "code": "601318.SH", "qty": 300, "cost": 48.5, "price": 46.2, "pnl": -690, "pnlPct": -4.74},
                    {"Name": "招商银行", "code": "600036.SH", "qty": 400, "cost": 35.8, "price": 36.5, "pnl": 280, "pnlPct": 1.96}
                ]
            }
        ],
        "totals": {
            "total_assets": 2847560.80,
            "total_market": 2568912.50,
            "total_cash": 278648.30,
            "stock_value": 2568912.50,
            "total_pnl": 125680.50,
            "total_pnl_pct": 4.62,
            "today_pnl": 28456.80,
            "position_pct": 90.2
        },
        "updateTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
}

DECISION_DATA = {
    "success": True,
    "data": {
        "updateTime": datetime.now().strftime('%H:%M'),
        "market_env": {
            "level": "震荡偏多",
            "score": 65,
            "position_limit": 80,
            "dimensions": {
                "trend": {"score": 70, "status": "上升趋势"},
                "money": {"score": 60, "status": "资金流入"},
                "emotion": {"score": 65, "status": "情绪中性"}
            },
            "details": {
                "ma_signal": "多头排列",
                "volume_status": "放量",
                "support_level": "3200点"
            }
        },
        "signal": "谨慎乐观",
        "suggestions": [
            {"priority": "高", "action": "加仓腾讯", "reason": "港股反弹，技术面突破"},
            {"priority": "中", "action": "减仓平安", "reason": "保险板块承压"},
            {"priority": "中", "action": "持有茅台", "reason": "白酒旺季临近"},
            {"priority": "低", "action": "关注宁德", "reason": "新能源政策利好"}
        ],
        "position_rules": {
            "current": 90.2,
            "target": 85,
            "max": 80,
            "min": 60
        },
        "cross_risk": {
            "risk_level": "中等",
            "exposure": {"stock": 85, "bond": 10, "cash": 5}
        }
    }
}

def handler(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    
    # CORS headers
    headers = [
        ('Content-Type', 'application/json; charset=utf-8'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'),
        ('Access-Control-Allow-Headers', 'Content-Type'),
    ]
    
    if path == '/api/health':
        body = json.dumps({"status": "ok", "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    elif path == '/api/portfolio':
        body = json.dumps(PORTFOLIO_DATA)
    elif path == '/api/decision-engine':
        body = json.dumps(DECISION_DATA)
    elif path == '/api/kpi':
        body = json.dumps({
            "success": True,
            "data": {
                "win_rate": {"value": 68.5, "label": "胜率", "color": "green", "type": "percent"},
                "profit_factor": {"value": 2.35, "label": "盈亏比", "color": "green", "type": "number"},
                "max_drawdown": {"value": -12.8, "label": "最大回撤", "color": "red", "type": "percent"},
                "sharpe": {"value": 1.85, "label": "夏普比率", "color": "green", "type": "number"}
            }
        })
    else:
        start_response('404', [('Content-Type', 'text/plain')])
        return [b'Not Found']
    
    start_response('200', headers)
    return [body.encode('utf-8')]
