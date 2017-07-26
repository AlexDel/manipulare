(function() {
	angular.module('bias', []);
	angular.module('bias')
	.component('biasWrapper',{
		templateUrl: '/static/biasWrapper.html',
		controller: BiasWrapperCtrl
	}).component('biasForm', {
		templateUrl: '/static/biasFrom.html',
		bindings: {
			text: '=',
			code: '=',
			onSubmit: '&'
		}
	});



	function BiasWrapperCtrl ($http) {
		var ctrl = this;

		ctrl.text = '';
		ctrl.code = '';
		ctrl.resultFetched = false;
		ctrl.result = null;

		this.checkText = function () {
			$http.post('api/text/estimate', {code: this.code, text: this.text}).then(function(payload) {
				ctrl.resultFetched = true;
				ctrl.result = payload.data;
			})
		}
	}

})();