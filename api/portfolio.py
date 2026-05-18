from datetime import datetime
import json

def handler(environ, start_response):
    data = {
        "success": True,
        "data": {
            "accounts": [
                {"key": "guolian", "label": "国联", "stocks": [
                    {"name": "腾讯控股", "code": "00700.HK", "qty": 100, "cost": 380.5, "price": 385.2, "pnl": 470, "pnlPct": 1.24},
                    {"name": "阿里巴巴", "code": "09988.HK", "qty": 200, "cost": 85.3, "price": 82.1, "pnl": -640, "pnlPct": -3.75},
                    {"name": "美团", "code": "03690.HK", "qty": 150, "cost": 120.8, "price": 125.5, "pnl": 705, "pnlPct": 3.89}
                ]},
                {"key": "guoxin", "label": "国信", "stocks": [
                    {"name": "贵州茅台", "code": "600519.SH", "qty": 50, "cost": 1680.0, "price": 1725.5, "pnl": 2275, "pnlPct": 2.71},
                    {"name": "宁德时代", "code": "300750.SZ", "qty": 80, "cost": 210.5, "price": 208.3, "pnl": -176, "pnlPct": -1.05}
                ]},
                {"key": "guangfa", "label": "广发", "stocks": [
                    {"name": "比亚迪", "code": "002594.SZ", "qty": 120, "cost": 245.8, "price": 258.6, "pnl": 1536, "pnlPct": 5.21},
                    {"name": "五粮液", "code": "000858.SZ", "qty": 100, "cost": 158.2, "price": 152.8, "pnl": -540, "pnlPct": -3.41}
                ]},
                {"key": "huatai", "label": "华泰", "stocks": [
                    {"name": "中国平安", "code": "601318.SH", "qty": 300, "cost": 48.5, "price": 46.2, "pnl": -690, "pnlPct": -4.74},
                    {"name": "招商银行", "code": "600036.SH", "qty": 400, "cost": 35.8, "price": 36.5, "pnl": 280, "pnlPct": 1.96}
                ]}
            ],
            "totals": {
                "total_assets": 2847560.80, "total_market": 2568912.50, "total_cash": 278648.30,
                "stock_value": 2568912.50, "total_pnl": 125680.50, "total_pnl_pct": 4.62,
                "today_pnl": 28456.80, "position_pct": 90.2
            },
            "updateTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    }
    body = json.dumps(data)
    start_response('200', [('Content-Type', 'application/json; charset=utf-8'), ('Access-Control-Allow-Origin', '*')])
    return [body.encode('utf-8')]
