<script>
	import PostList from './componentes/PostList.svelte'
	import PostDetail from './componentes/PostDetail.svelte'
</script>

<main>
	<PostList />
	<PostDetail />
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

