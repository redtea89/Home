<script>
	let visible = false;

	function typewriter(node, { speed = 1 }) {
		const valid = (
			node.childNodes.length === 1 &&
			node.childNodes[0].nodeType === Node.TEXT_NODE
		);

		if (!valid) {
			throw new Error(`This transition only works on elements with a single text node child`);
		}

		const text = node.textContent;
		const duration = text.length / (speed * 0.01);

		return {
			duration,
			tick: t => {
				const i = ~~(text.length * t);
				node.textContent = text.slice(0, i);
			}
		};
	}
</script>

<label>
	<input type="checkbox" bind:checked={visible}>
	오잉 버튼이 있네
</label>

{#if visible}
	<p transition:typewriter>
		설마 이 버튼을 누르셨나요? 사실 이 버튼의 의미는                  있습니다. 그건 바로           .     .    60초 후에..            설마 지금까지 기다렸나요?      만나서 만갑습니다-!
	</p>
{/if}