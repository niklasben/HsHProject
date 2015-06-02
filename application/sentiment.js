var twitter = angular.module('myApp', ['ui.bootstrap','nvd3ChartDirectives']);

twitter.controller('myController', function($rootScope, $scope){
	$scope.view = "";
	$scope.graphID = "active";
	$scope.tlistID = "topics";
	$scope.clistID = "countries";
	$scope.selectView = function(view){
		$scope.view = view;
		$scope.graphData = [];
		$scope.selectedGraphs = [];
		$scope.selectedCountries = [];
		$scope.selectedTopics = [];
		$scope.listData = [];
		if(view == ''){
			$scope.selectedData = {
				topic: "",
				country: "",
				values: ""
			};
			$scope.topics = [];
			$scope.countries = [];
		}
		if(view == 'countries'){
			if($scope.selectedData.country){
				$scope.selectedData = {
					topic: "",
					country: "",
					values: ""
				};
			}
			$scope.showCountries();
		}
		if(view == 'topics'){
			if($scope.selectedData.topic){
				$scope.selectedData = {
					topic: "",
					country: "",
					values: ""
				};
			}
			$scope.showTopics();
			
		}
	}
	$scope.topics = [];
	$scope.countries = [];
	$scope.selectedData = {
		topic: "",
		country: "",
		values: ""
	};
	$scope.showTopics = function(){
		if(!$scope.topics.length){
			var ind = 0;
			angular.forEach($scope.data, function(d){
				var sum = 0;
				angular.forEach(d.content, function(c){
					sum += c.rates.positive + c.rates.neutral + c.rates.negative;
				})
				$scope.topics.push({name: d.value, tweets: sum, index: ind});
				ind++;
			});
			if(!$scope.selectedData.country){
				$scope.topics = $scope.topics.sort(function(a,b){
					return b.tweets-a.tweets;
				})
				angular.forEach($scope.topics, function(t){
					var data = {
						key: t.name,
						values:[[t.name, t.tweets]]
					}
					$scope.listData.push(data);
				});
			}
		}
		if($scope.topics.length && $scope.selectedData.country){
			$scope.topics = [];
			var ind = 0;
			angular.forEach($scope.data, function(d){
				angular.forEach(d.content, function(c){
					if(c.value == $scope.selectedData.country.value){
							var sum = c.rates.positive + c.rates.neutral + c.rates.negative;
							$scope.topics.push({ name: d.value, tweets: sum, index: ind });
					}
				});
				ind++;
			});
		}
	};

	$scope.$watch('graphData', function(){
	},true);
	$scope.graphData = [];
	$scope.selectedGraphs = [];
	$scope.selectedCountries = [];
	$scope.selectedTopics = [];
	$scope.listData = [];
	$scope.selectTopic = function(index){
		$scope.selectedData.topic = {
			value: $scope.data[index].value,
			index: index
		}
		var duplicate = false;
		var dpos = "";
		if($scope.selectedData.country){
			var i = 0;
			angular.forEach($scope.selectedGraphs, function(v, k){
				if(v.key == $scope.selectedData.topic.value){
					duplicate = true;
					dpos = i;
				}
				i++;
			})
			if(duplicate == false){
				var cindex = $scope.selectedData.country.index;
				console.log(cindex);
				$scope.selectedTopics[$scope.selectedData.topic.value] = true;
				$scope.selectedData.values = angular.copy($scope.data[index].content[cindex].rates);
				console.log($scope.data[index].value + " " + $scope.selectedData.values.positive + " " + $scope.selectedData.values.negative);
				var rpos = $scope.selectedData.values.positive / ($scope.selectedData.values.positive + $scope.selectedData.values.negative) * 100;
				var rneg = $scope.selectedData.values.negative / ($scope.selectedData.values.positive + $scope.selectedData.values.negative) * 100;
				var data = 	{
						key: $scope.selectedData.topic.value,
						values: [[ "positiv", rpos ],[ "negativ", rneg ]]
					}
				$scope.selectedGraphs.push(data);
				$scope.graphData = angular.copy($scope.selectedGraphs);
			}else{
				$scope.selectedTopics[$scope.selectedData.topic.value] = false;
				$scope.selectedGraphs.splice(dpos, 1);
				$scope.graphData = angular.copy($scope.selectedGraphs);
			}
		}else{
			$scope.selectView('countries');
		}
	}
	$scope.showCountries = function(){
		if(!$scope.countries.length){
			var dupe = 0;
			var ind = 0;
			angular.forEach($scope.data, function(data){

				angular.forEach(data.content, function(c) {
					angular.forEach($scope.countries, function(v){
						if(v.name == c.value){
							dupe = 1;
						}
					});
					if(dupe == 0){
						var sum = 0;
						angular.forEach($scope.data, function(d){
							angular.forEach(d.content, function(con){
								if(con.value == c.value){
									sum += con.rates.positive + con.rates.neutral + con.rates.negative;
								}
							})
						})
						$scope.countries.push({name: c.value, tweets: sum, index: ind });
						ind++;
					}
				});
			});
			if(!$scope.selectedData.topic){
				$scope.countries = $scope.countries.sort(function(a,b){
					return b.tweets-a.tweets;
				})
				angular.forEach($scope.countries, function(c){
					var data = {
						key: c.name,
						values:[[c.name, c.tweets]]
					}
					$scope.listData.push(data);
				});
			}
		}
		if($scope.countries.length && $scope.selectedData.topic){
			$scope.countries = [];
			var sum = 0;
			var ind = 0;
			angular.forEach($scope.data, function(d){
				if(d.value == $scope.selectedData.topic.value){
					angular.forEach(d.content, function(c){
						sum = c.rates.positive + c.rates.neutral + c.rates.negative;
						$scope.countries.push({ name: c.value, tweets: sum, index: ind });
						ind++;
					})
				}
			});
		}
	};
	
	$scope.selectCountry = function(index){
		$scope.selectedData.country = {
			value: $scope.countries[index].name,
			index: index
		}
		var duplicate = false;
		var dpos = "";
		if($scope.selectedData.topic){
			var i = 0;
			angular.forEach($scope.selectedGraphs, function(v, k){
				if(v.key == $scope.selectedData.country.value){
					duplicate = true;
					dpos = i;
				}
				i++;
			})
			if(duplicate == false){	
				var tindex = $scope.selectedData.topic.index;
				$scope.selectedCountries[$scope.selectedData.country.value] = true;
				$scope.selectedData.values = angular.copy($scope.data[tindex].content[index].rates);
				var rpos = $scope.selectedData.values.positive / ($scope.selectedData.values.positive + $scope.selectedData.values.negative) * 100;
				var rneg = $scope.selectedData.values.negative / ($scope.selectedData.values.positive + $scope.selectedData.values.negative) * 100;
				var data = 	{
						key: $scope.selectedData.country.value,
						values: [[ "positiv",  rpos ],[  "negativ",  rneg ]]
					}
				$scope.selectedGraphs.push(data);
				$scope.graphData = angular.copy($scope.selectedGraphs);
			}else{
				$scope.selectedCountries[$scope.selectedData.country.value] = false;
				$scope.selectedGraphs.splice(dpos, 1);
				$scope.graphData = angular.copy($scope.selectedGraphs);
			}
		}else{
			$scope.selectView('topics');
		}
	}
	$scope.showGraph = function(values){
	}
});
twitter.run(function($rootScope, $http){
	$rootScope.data = [];
	$http.get('data/input.json').success(function(data){
		$rootScope.data = data;
	});
});
