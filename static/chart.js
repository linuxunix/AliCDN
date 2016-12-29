/**
 * @namespace Chart
 */
var Chart = require(http://localhost:8000/static/core/core.js')();

require(http://localhost:8000/static/core/core.helpers')(Chart);
require(http://localhost:8000/static/core/core.canvasHelpers')(Chart);
require(http://localhost:8000/static/core/core.plugin.js')(Chart);
require(http://localhost:8000/static/core/core.element')(Chart);
require(http://localhost:8000/static/core/core.animation')(Chart);
require(http://localhost:8000/static/core/core.controller')(Chart);
require(http://localhost:8000/static/core/core.datasetController')(Chart);
require(http://localhost:8000/static/core/core.layoutService')(Chart);
require(http://localhost:8000/static/core/core.scaleService')(Chart);
require(http://localhost:8000/static/core/core.ticks.js')(Chart);
require(http://localhost:8000/static/core/core.scale')(Chart);
require(http://localhost:8000/static/core/core.title')(Chart);
require(http://localhost:8000/static/core/core.legend')(Chart);
require(http://localhost:8000/static/core/core.interaction')(Chart);
require(http://localhost:8000/static/core/core.tooltip')(Chart);

require(http://localhost:8000/static/elements/element.arc')(Chart);
require(http://localhost:8000/static/elements/element.line')(Chart);
require(http://localhost:8000/static/elements/element.point')(Chart);
require(http://localhost:8000/static/elements/element.rectangle')(Chart);

require(http://localhost:8000/static/scales/scale.linearbase.js')(Chart);
require(http://localhost:8000/static/scales/scale.category')(Chart);
require(http://localhost:8000/static/scales/scale.linear')(Chart);
require(http://localhost:8000/static/scales/scale.logarithmic')(Chart);
require(http://localhost:8000/static/scales/scale.radialLinear')(Chart);
require(http://localhost:8000/static/scales/scale.time')(Chart);

// Controllers must be loaded after elements
// See Chart.core.datasetController.dataElementType
require(http://localhost:8000/static/controllers/controller.bar')(Chart);
require(http://localhost:8000/static/controllers/controller.bubble')(Chart);
require(http://localhost:8000/static/controllers/controller.doughnut')(Chart);
require(http://localhost:8000/static/controllers/controller.line')(Chart);
require(http://localhost:8000/static/controllers/controller.polarArea')(Chart);
require(http://localhost:8000/static/controllers/controller.radar')(Chart);

require(http://localhost:8000/static/charts/Chart.Bar')(Chart);
require(http://localhost:8000/static/charts/Chart.Bubble')(Chart);
require(http://localhost:8000/static/charts/Chart.Doughnut')(Chart);
require(http://localhost:8000/static/charts/Chart.Line')(Chart);
require(http://localhost:8000/static/charts/Chart.PolarArea')(Chart);
require(http://localhost:8000/static/charts/Chart.Radar')(Chart);
require(http://localhost:8000/static/charts/Chart.Scatter')(Chart);

window.Chart = module.exports = Chart;
