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

		this.text = '';
		this.code = '';

		this.checkText = function () {
			$http.post('api/text/estimate', {code: this.code, text: this.text})
		}
	}

})();