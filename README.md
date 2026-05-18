# 投资驾驶舱 - Vercel部署

## 快速部署

### 1. GitHub仓库
代码已准备好推送到 GitHub：
```
https://github.com/miaodesign/investment-cockpit
```

### 2. 部署到Vercel

1. 打开 https://vercel.com/new
2. 点击 "Import Git Repository"
3. 选择 `investment-cockpit` 仓库
4. 点击 "Deploy"

5分钟后即可获得永久访问地址，例如：
```
https://investment-cockpit.vercel.app
```

## 数据修改

编辑 `api/portfolio.py` 和 `api/decision-engine.py` 中的数据即可。

## 本地测试

```bash
cd cockpit_deploy
vercel dev
```

然后访问 http://localhost:3000
