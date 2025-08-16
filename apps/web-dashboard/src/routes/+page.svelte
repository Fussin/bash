<script lang="ts">
	import { onMount } from 'svelte';

	let status: 'checking' | 'ok' | 'error' = 'checking';

	onMount(async () => {
		try {
            // The vite.config.js proxies this request to the API Gateway in dev mode
			const response = await fetch('/api/health');
			if (response.ok) {
				status = 'ok';
			} else {
				status = 'error';
			}
		} catch (e) {
			status = 'error';
		}
	});
</script>

<main style="font-family: sans-serif; padding: 2em;">
    <h1>Project Chimera</h1>
    <p>Web Dashboard for monitoring and initiating security scans.</p>

    <p>
        API Gateway Status:
        {#if status === 'checking'}
            <span>Checking...</span>
        {:else if status === 'ok'}
            <span style="color: green;">● Online</span>
        {:else}
            <span style="color: red;">● Offline</span>
        {/if}
    </p>
</main>
