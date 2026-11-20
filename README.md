# 今日宜晒 · 微信休闲小游戏

> P1a 浏览器纵切原型，尚未接入微信小游戏 SDK，也没有真实广告。

## 在线试玩

在 GitHub 仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。工作流 `.github/workflows/pages.yml` 将 `site/` 目录发布到 Pages。

在 Pages 首次成功部署后，公开网址为：
https://jyy521521.github.io/jinri-yishai/

## 目录

- `site/index.html`：唯一网页游戏源码（P1a）
- `site/assets/icon.svg`：原创游戏矢量图标
- `docs/`：原始设计案、总控文档 v1.0、原创美术规范、批量开发任务单
- `tests/`：自动验收、已知限制
- `.github/workflows/pages.yml`：GitHub Pages 自动发布工作流

## 当前进度

- [x] 纵切玩法：六时辰天气、摆/移/盖/收、结算
- [x] 原创基础 UI、图标、静态页面
- [x] 本地浏览器冒烟测试
- [ ] 五个教学关与新手体验
- [ ] 更精细的美术资产及动画
- [ ] 真实微信小游戏迁移、广告 SDK、资质审核

## 协作规范

**本仓库为《今日宜晒》唯一代码权威。** 先在 `feat/...` 分支开发，测试通过后经 PR 合入 `main`，合并后自动重新发布 Pages。不要随意把未验收玩法推进 `main`。

不能仅凭 Pages 显示部署完成就认为游戏 QA 通过；必须再验证手机 Safari/Chrome 的摆放、结算和存档。

## 本地预览

`python3 -m http.server 8080 --directory site`，在浏览器打开 http://localhost:8080 。
