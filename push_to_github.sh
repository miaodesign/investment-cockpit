#!/bin/bash
echo "=== 推送到GitHub ==="
echo ""
echo "请在浏览器中登录GitHub，然后在此输入您的GitHub用户名和Token"
echo "（Token获取方式：https://github.com/settings/tokens/new）"
echo ""
read -p "GitHub用户名: " username
read -sp "GitHub Token: " token
echo ""

cd "$(dirname "$0")"

# 使用token推送到远程
git remote remove origin 2>/dev/null
git remote add origin "https://${username}:${token}@github.com/miaodesign/investment-cockpit.git"

# 推送到main分支
git branch -m main
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "下一步：部署到Vercel"
    echo "1. 打开 https://vercel.com/new"
    echo "2. 导入 investment-cockpit 仓库"
    echo "3. 点击 Deploy"
else
    echo ""
    echo "❌ 推送失败，请检查用户名和Token"
fi
