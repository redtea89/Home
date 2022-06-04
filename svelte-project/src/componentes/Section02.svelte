<script>
	import { time, elapsed } from '../utils/stores';

	const formatter = new Intl.DateTimeFormat('en', {
		hour12: true,
		hour: 'numeric',
		minute: '2-digit',
		second: '2-digit'
	});
</script>

<h3>현재시간 {formatter.format($time)}</h3>

<p>
	이 페이지가 열린지 
	{$elapsed} {$elapsed === 1 ? '초' : '초'} 지났습니다.
</p>