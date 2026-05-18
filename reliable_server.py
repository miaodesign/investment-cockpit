#!/usr/bin/env python3
"""
可靠的投资驾驶舱服务器 - 内嵌隧道功能
无需外部SSH，直接提供公网访问
"""
import http.server
import socketserver
import json
import os
import sys
import threading
import time
import urllib.request
import urllib.error
from datetime import datetime

# 配置
PORT = 8080
PUBLIC_URL = None

# 导入原有的数据模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 模拟数据（内嵌，不依赖外部API）
PORTFOLIO_DATA = {
    "success": True,
    "data": {
        "accounts": [
            {
                "key": "guolian",
                "label": "国联",
                "stocks": [
                    {"name": "腾讯控股", "code": "00700.HK", "qty": 100, "cost": 380.5, "price": 385.2, "pnl": 470, "pnlPct": 1.24},
                    {"name": "阿里巴巴", "code": "09988.HK", "qty": 200, "cost": 85.3, "price": 82.1, "pnl": -640, "pnlPct": -3.75},
                    {"name": "美团", "code": "03690.HK", "qty": 150, "cost": 120.8, "price": 125.5, "pnl": 705, "pnlPct": 3.89}
                ]
            },
            {
                "key": "guoxin",
                "label": "国信",
                "stocks": [
                    {"name": "贵州茅台", "code": "600519.SH", "qty": 50, "cost": 1680.0, "price": 1725.5, "pnl": 2275, "pnlPct": 2.71},
                    {"name": "宁德时代", "code": "300750.SZ", "qty": 80, "cost": 210.5, "price": 208.3, "pnl": -176, "pnlPct": -1.05}
                ]
            },
            {
                "key": "guangfa",
                "label": "广发",
                "stocks": [
                    {"name": "比亚迪", "code": "002594.SZ", "qty": 120, "cost": 245.8, "price": 258.6, "pnl": 1536, "pnlPct": 5.21},
                    {"name": "五粮液", "code": "000858.SZ", "qty": 100, "cost": 158.2, "price": 152.8, "pnl": -540, "pnlPct": -3.41}
                ]
            },
            {
                "key": "huatai",
                "label": "华泰",
                "stocks": [
                    {"name": "中国平安", "code": "601318.SH", "qty": 300, "cost": 48.5, "price": 46.2, "pnl": -690, "pnlPct": -4.74},
                    {"name": "招商银行", "code": "600036.SH", "qty": 400, "cost": 35.8, "price": 36.5, "pnl": 280, "pnlPct": 1.96}
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

class APIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # API路由
        if self.path == '/api/health':
            self.send_json({"status": "ok", "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return
        
        elif self.path == '/api/portfolio':
            self.send_json(PORTFOLIO_DATA)
            return
        
        elif self.path == '/api/decision-engine':
            self.send_json(DECISION_DATA)
            return
        
        elif self.path == '/api/kpi':
            self.send_json({
                "success": True,
                "data": {
                    "win_rate": {"value": 68.5, "label": "胜率", "color": "green", "type": "percent"},
                    "profit_factor": {"value": 2.35, "label": "盈亏比", "color": "green", "type": "number"},
                    "max_drawdown": {"value": -12.8, "label": "最大回撤", "color": "red", "type": "percent"},
                    "sharpe": {"value": 1.85, "label": "夏普比率", "color": "green", "type": "number"}
                }
            })
            return
        
        elif self.path == '/api/risk-budget':
            self.send_json({
                "success": True,
                "data": {
                    "total_budget": 100,
                    "used": 85,
                    "available": 15,
                    "by_sector": {
                        "科技": 35,
                        "消费": 25,
                        "金融": 15,
                        "医药": 10
                    }
                }
            })
            return
        
        elif self.path == '/api/a-trend-table':
            self.send_json({
                "success": True,
                "data": {
                    "trends": [
                        {"name": "上证指数", "value": 3256.8, "change": 1.25, "trend": "up"},
                        {"name": "深证成指", "value": 10568.2, "change": 0.89, "trend": "up"},
                        {"name": "创业板指", "value": 2156.4, "change": -0.35, "trend": "down"},
                        {"name": "恒生指数", "value": 18562.3, "change": 2.15, "trend": "up"}
                    ]
                }
            })
            return
        
        elif self.path == '/api/daily-report':
            self.send_json({
                "success": True,
                "data": {
                    "date": datetime.now().strftime('%Y-%m-%d'),
                    "summary": "今日市场震荡上行，科技股领涨",
                    "highlights": ["港股反弹", "北向资金流入", "成交量放大"],
                    "alerts": ["注意美联储议息会议", "关注汇率波动"]
                }
            })
            return
        
        # 静态文件服务
        elif self.path == '/':
            self.path = '/cockpit.html'
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())
    
    def log_message(self, format, *args):
        # 简化日志
        if '/api/' in args[0]:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {args[0]}")

def start_tunnel():
    """尝试建立隧道"""
    global PUBLIC_URL
    
    # 尝试Serveo
    print("[隧道] 尝试Serveo...")
    try:
        import subprocess
        proc = subprocess.Popen(
            ['ssh', '-o', 'StrictHostKeyChecking=no', 
             '-o', 'ServerAliveInterval=30',
             '-R', '80:localhost:8080', 'serveo.net'],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True
        )
        
        # 读取URL
        import select
        import fcntl
        import os
        
        fd = proc.stdout.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        
        for _ in range(30):
            time.sleep(1)
            try:
                line = proc.stdout.read()
                if line:
                    print(f"[隧道] {line.strip()}")
                    import re
                    m = re.search(r'https://[^\s]+', line)
                    if m:
                        PUBLIC_URL = m.group(0)
                        print(f"\n✅ 公网地址: {PUBLIC_URL}")
                        print(f"✅ 本地地址: http://localhost:8080\n")
                        return True
            except:
                pass
    except Exception as e:
        print(f"[隧道] Serveo失败: {e}")
    
    return False

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 50)
    print("投资驾驶舱 - 可靠服务器")
    print("=" * 50)
    
    # 启动HTTP服务器
    handler = APIHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    print(f"\n✅ HTTP服务器启动: http://localhost:{PORT}")
    
    # 尝试启动隧道（后台线程）
    tunnel_thread = threading.Thread(target=start_tunnel, daemon=True)
    tunnel_thread.start()
    
    print("\n可用API:")
    print(f"  - http://localhost:{PORT}/api/health")
    print(f"  - http://localhost:{PORT}/api/portfolio")
    print(f"  - http://localhost:{PORT}/api/decision-engine")
    print(f"\n页面地址: http://localhost:{PORT}/cockpit.html")
    print("=" * 50)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器停止")
        httpd.shutdown()

if __name__ == '__main__':
    main()
