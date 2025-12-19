1) 启动后端
>pip install "fastapi[all]"


uvicorn main:app --reload --host 0.0.0.0 --port 8000



2) 启动前端

1️⃣ 安装 Node.js 和 npm

官网：https://nodejs.org

下载 LTS 版本（18+），安装完成后验证：

node -v
npm -v


2️⃣ 创建 Vite + React 项目
npm create vite@latest my-app

chosse frame work: React:
-------------------------------------------------------------------------
如果你的目标是 React + JSX + 热更新，在 Vite 创建项目时，框架（framework）选：

React


Vue → Vue.js 框架，不是你想用的

Preact → React 精简版，不是必须

Vanilla → 纯 JS，没有框架

✅ 下一步选择 Variant（类型）：

JavaScript → 普通 JS

TypeScript → TypeScript
 Select a framework:
|  React
|
o  Select a variant:
|  TypeScript + SWC
|
*  Use rolldown-vite (Experimental)?:
|    Yes
|  > No
-----------------------------------------

cd my-app

3️⃣ 安装依赖
npm install


npm run dev -- --port 5173 --host
--host → 让 Vite 绑定所有网卡（IPv4 + IPv6），不仅限于 [::1]，解决了你之前浏览器打不开的问题

